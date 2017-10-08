from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
from datetime import datetime

import numpy as np
import tensorflow as tf
import os
# remove warning
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

from scripts.label_image import *
import pandas as pd

#PROJECT_PATH = "D:\\00_work\\data\\kaggle datasets\\DR\\"
#PROJECT_PATH = "/mnt/d/00_work/data/kaggle datasets/DR/"

def cal_accuracy(file_list, top_dict, class_no=2):
    df = pd.read_csv(PROJECT_PATH+'trainLabels.csv')
    correct = 0
    num = len(file_list)
    predict_and_label ={'predict':[], 'label':[]}
    for f in file_list:
        idx = f[0:len(f)-5]
        if class_no == 2:
            try:
                correct_label = int(df[df.image == idx].level.values>0)
                predict_and_label['predict'].append(top_dict[idx])
                predict_and_label['label'].append(correct_label)
            except Exception:
                pass
            
        if correct_label == top_dict[idx]:
            correct+=1
    
    x = tf.placeholder(tf.int32, )
    y = tf.placeholder(tf.int32, )
    rec, rec_op  = tf.metrics.recall(labels=x, predictions=y)
    pre, pre_op  = tf.metrics.precision(labels=x, predictions=y)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        P = sess.run(pre_op, feed_dict={x: predict_and_label['label'],y: predict_and_label['predict']} ) 
        R = sess.run(rec_op, feed_dict={x: predict_and_label['label'],y: predict_and_label['predict']} ) 
    
    print('CORRECT \t{0}/{1}'.format(correct, num))
    print("PRECISION \t{0}".format(P))
    print("RECALL \t\t{0}".format(R))
    print("F1 \t\t{0}".format((2*P*R)/(P+R)))
    print("ACC \t\t{0}".format(correct/num))
    
    
if __name__ == "__main__":
    model_file = "tf_files/retrained_graph.pb"
    label_file = "tf_files/retrained_labels.txt"
    input_height = 299
    input_width = 299
    input_mean = 128
    input_std = 128
    input_layer = "Mul"
    output_layer = "final_result"

    parser = argparse.ArgumentParser()
    parser.add_argument("--project", help="project path")
    parser.add_argument("--image", help="image to be processed")
    parser.add_argument("--graph", help="graph/model to be executed")
    parser.add_argument("--labels", help="name of file containing labels")
    parser.add_argument("--input_height", type=int, help="input height")
    parser.add_argument("--input_width", type=int, help="input width")
    parser.add_argument("--input_mean", type=int, help="input mean")
    parser.add_argument("--input_std", type=int, help="input std")
    parser.add_argument("--input_layer", help="name of input layer")
    parser.add_argument("--output_layer", help="name of output layer")
    args = parser.parse_args()

    if args.project:
        PROJECT_PATH = args.project
    if args.graph:
        model_file = args.graph
    if args.image:
        file_name = args.image
    if args.labels:
        label_file = args.labels
    if args.input_height:
        input_height = args.input_height
    if args.input_width:
        input_width = args.input_width
    if args.input_mean:
        input_mean = args.input_mean
    if args.input_std:
        input_std = args.input_std
    if args.input_layer:
        input_layer = args.input_layer
    if args.output_layer:
        output_layer = args.output_layer
    
    test_path = PROJECT_PATH + 'test_1024/'
    file_list = os.listdir(test_path)
    file_name = test_path + file_list[0]
    key_list = []
    value_list = []
    graph = load_graph(model_file)
    labels = load_labels(label_file)
    input_name = "import/" + input_layer
    output_name = "import/" + output_layer
    input_operation = graph.get_operation_by_name(input_name);
    output_operation = graph.get_operation_by_name(output_name);
    count = 0
    num = len(file_list)
    
    print(datetime.now())
    for f in file_list:
        src = test_path + f
        t = read_tensor_from_image_file(src,
                                  input_height=input_height,
                                  input_width=input_width,
                                  input_mean=input_mean,
                                  input_std=input_std)


        with tf.Session(graph=graph) as sess:
            results = sess.run(output_operation.outputs[0],
                          {input_operation.outputs[0]: t})
                          
        results = np.squeeze(results)
        top_k = results.argsort()[-5:][::-1]
        key_list.append(f[0:(len(f)-5)])
        yhat = int(results[1]>0.4)
        #value_list.append(int(labels[list(results).index(max(results))]))
        value_list.append(yhat)
            
        count+=1
        if count%20 == 0:
            print("Done {0}/{1}".format(count, num))
        #if count==100:
            #break
            
            
    top_dict = dict(zip(key_list, value_list))
    cal_accuracy(file_list, top_dict)
                
    print(datetime.now())
            
            