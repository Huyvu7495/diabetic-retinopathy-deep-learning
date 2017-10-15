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

def read_tensor_from_image_list(file_list, input_height=299, input_width=299,
				input_mean=0, input_std=255):
    input_name = "file_reader"
    output_name = "normalized"
    result=list()
    count=0
    num = len(file_list)
    sess = tf.Session()
    for file_name in file_list:
        file_reader = tf.read_file(file_name, input_name)
        if file_name.endswith(".png"):
            image_reader = tf.image.decode_png(file_reader, channels = 3,
                                             name='png_reader')
        elif file_name.endswith(".gif"):
            image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                        name='gif_reader'))
        elif file_name.endswith(".bmp"):
            image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
        else:
            image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                              name='jpeg_reader')
        float_caster = tf.cast(image_reader, tf.float32)
        dims_expander = tf.expand_dims(float_caster, 0);
        resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
        normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
        result.append(sess.run(normalized))
        count+=1
        if count%20 == 0:
            print("READ {0}/{1}".format(count, num))
    
    return result
  
def cal_accuracy(file_list, top_dict, class_no=2):
    df = pd.read_csv(PROJECT_PATH+'trainLabels.csv')
    correct = 0
    num = len(file_list)
    predict_and_label ={'predict':[], 'label':[]}
    for f in file_list:
        idx = f[0:len(f)-5]
        if class_no == 2:
            try:
                correct_label = int(df[df.image == idx].level.values)
                predict_and_label['predict'].append(top_dict[idx])
                predict_and_label['label'].append(correct_label)
            except Exception:
                pass
            
        if correct_label == top_dict[idx]:
            correct+=1
    #for (p, l) in zip(predict_and_label['predict'], predict_and_label['label']):
    #    if p==4:
    #        if p==l:
    #            TP+=1
    #        else:
    #            FP+=1
    #    else:
    #        if p==l:
    #            TN+=1
    #        elif l==4:
    #            FN+=1
    
    x = tf.placeholder(tf.int32, )
    y = tf.placeholder(tf.int32, )
    rec, rec_op  = tf.metrics.recall(labels=x, predictions=y)
    pre, pre_op  = tf.metrics.precision(labels=x, predictions=y)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        P = sess.run(pre_op, feed_dict={x: predict_and_label['label'],y: predict_and_label['predict']} ) 
        R = sess.run(rec_op, feed_dict={x: predict_and_label['label'],y: predict_and_label['predict']} ) 
    
    try:  
    #    P = TP/(TP+FP)
    #    R = TP/(TP+FN)
        F1 = (2*P*R)/(P+R)
    except ZeroDivisionError:
        P = 0
        R = 0
        F1 = 0
        
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
    parser.add_argument("--threshold", help="threshold for softmax")
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
    if args.project:
        threshold = float(args.threshold)
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
    
    test_path = PROJECT_PATH + 'test/'
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
    
    print("BEGIN ", datetime.now())
    #for f in file_list:
    #    src = test_path + f
    #    t = read_tensor_from_image_file(src,
    #                              input_height=input_height,
    #                              input_width=input_width,
    #                              input_mean=input_mean,
    #                              input_std=input_std)
    #
    #
    #    with tf.Session(graph=graph) as sess:
    #        results = sess.run(output_operation.outputs[0],
    #                      {input_operation.outputs[0]: t})
    #                      
    #    results = np.squeeze(results)
    #    top_k = results.argsort()[-5:][::-1]
    #    key_list.append(f[0:(len(f)-5)])
    #    yhat = int(results[0]>threshold)
    #    #value_list.append(int(labels[list(results).index(max(results))]))
    #    value_list.append(yhat)
    #        
    #    count+=1
    #    if count%20 == 0:
    #        print("Done {0}/{1}".format(count, num))
    #    #if count==100:
    #        #break
    t_list = list()
    results = list()
    image_list=list()
    for f in file_list:
        src = test_path + f
        key_list.append(f[0:(len(f)-5)])
        #image_list.append(src)
        
    #t_list = read_tensor_from_image_list(image_list,
    #                              input_height=input_height,
    #                              input_width=input_width,
    #                              input_mean=input_mean,
    #                              input_std=input_std)
                                  
        t_list.append(read_tensor_from_image_file(src,
                                  input_height=input_height,
                                  input_width=input_width,
                                  input_mean=input_mean,
                                  input_std=input_std)
                )
        count+=1
        if count%20 == 0:
            print("READ {0}/{1}".format(count, num))
    
    print("CALCULATING")
    with tf.Session(graph=graph) as sess:
        for t in t_list:
            results.append(sess.run(output_operation.outputs[0],
                          {input_operation.outputs[0]: t})
                           )   

        for r in results:
            tmp = np.squeeze(r)
            #top_k = r.argsort()[-5:][::-1]
            #yhat = int(tmp[0]>threshold)
#            yhat = int(labels[tmp.index(max(tmp))])
            yhat = int(labels[np.argmax(tmp)])
            value_list.append(yhat)
            
            
            
    top_dict = dict(zip(key_list, value_list))
    cal_accuracy(file_list, top_dict)
                
    print("FINISH ", datetime.now())
            
            