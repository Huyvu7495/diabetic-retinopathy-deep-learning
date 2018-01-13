from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
from datetime import datetime
from os import environ, listdir
# remove warning
environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import tensorflow as tf
from lib.label_image import *
import pandas as pd

config = tf.ConfigProto()
config.intra_op_parallelism_threads = 4
config.inter_op_parallelism_threads = 0


def max_count(a):
    return np.bincount(a).argmax()


def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
                                input_mean=0, input_std=255):
    input_name = "file_reader"
    output_name = "normalized"
    file_reader = tf.read_file(file_name, input_name)
    if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(file_reader, channels=3,
                                           name='png_reader')
    elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                      name='gif_reader'))
    elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
    else:
        image_reader = tf.image.decode_jpeg(file_reader, channels=3,
                                            name='jpeg_reader')
    float_caster = tf.cast(image_reader, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0)
    resized = tf.image.resize_bilinear(
        dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session(config=config)
    result = sess.run(normalized)

    return result


def cal_accuracy(files, dict_list):
    df = pd.read_csv(PROJECT_PATH + 'trainLabels.csv')
    num = len(files['dir'])
    TP, FP, TN, FN = 0, 0, 0, 0
    miss_class = list()
    data = {'p': list(), 'l': list()}
    for i in range(num):
        f = files['file'][i]
        d = files['dir'][i]
        idx = f[0:len(f) - 5]
        predict_list = list()

        correct = int(d)
        for d in dict_list:
            predict_list.append(d[idx])
        predict = max_count(predict_list)
        data['l'].append(correct)
        data['p'].append(predict)
        if correct == predict:
            TP += 1

    print("Last Predict {0}, Last Correct {1}".format(predict, correct))
    x = tf.placeholder(tf.int32, )
    y = tf.placeholder(tf.int32, )
    rec, rec_op = tf.metrics.recall(labels=x, predictions=y)
    pre, pre_op = tf.metrics.precision(labels=x, predictions=y)
    acc, acc_op = tf.metrics.accuracy(labels=x, predictions=y)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(tf.local_variables_initializer())
        P = sess.run(pre_op, feed_dict={x: data['l'], y: data['p']})
        R = sess.run(rec_op, feed_dict={x: data['l'], y: data['p']})
        ACC = sess.run(acc_op, feed_dict={x: data['l'], y: data['p']})

    print("ACC \t\t{0}".format(ACC))
    print('CORRECT \t{0}/{1}'.format(TP + TN, num))


if __name__ == "__main__":
    model_file="tf_files/retrained_graph.pb"
    label_file="tf_files/retrained_labels.txt"
    input_height=299
    input_width=299
    input_mean=128
    input_std=128
    input_layer="Mul"
    output_layer="final_result"

    parser=argparse.ArgumentParser()
    parser.add_argument("--project", help="project path")
    parser.add_argument("--testpath", help="test folder path")
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
    args=parser.parse_args()

    if args.project:
        PROJECT_PATH=args.project
    if args.threshold:
        threshold=float(args.threshold)
    if args.testpath:
        root_path=args.testpath
    else:
        root_path=PROJECT_PATH + 'test/'
    if args.graph:
        model_file=args.graph
    if args.image:
        file_name=args.image
    if args.labels:
        label_file=args.labels
    if args.input_height:
        input_height=args.input_height
    if args.input_width:
        input_width=args.input_width
    if args.input_mean:
        input_mean=args.input_mean
    if args.input_std:
        input_std=args.input_std
    if args.input_layer:
        input_layer=args.input_layer
    if args.output_layer:
        output_layer=args.output_layer

    graph_list=[model_file]
    label_list=[label_file]
    print(graph_list, label_list)
    dir_list=listdir(root_path)
    files={'file': list(),
             'dir': list()}

    for d in dir_list:
        tmp=listdir(root_path + d)

        for i in tmp:
            files['file'].append(i)
            files['dir'].append(d)

    num=len(files['dir'])
    dict_list=list()
    count=0

    value_list=list()
    results=list()
    print("BEGIN ", datetime.now())

    t_list=list()
    key_list=[]
    for i in range(num):
        f=files['file'][i]
        d=files['dir'][i]
        src=root_path + d + '/' + f
        t_list.append(read_tensor_from_image_file(src,
                                                  input_height=input_height,
                                                  input_width=input_width,
                                                  input_mean=input_mean,
                                                  input_std=input_std)
                      )
        count += 1
        if count % 125 == 0:
            print("READ {0}/{1}".format(count, num))
        if (count % 500 == 0 or i == num - 1):
            print("CALCULATING ", datetime.now())
            for model_idx in range(len(graph_list)):
                print(graph_list[model_idx], label_list[model_idx])

                graph=load_graph(graph_list[model_idx])
                labels=load_labels(label_list[model_idx])
                input_name="import/" + input_layer
                output_name="import/" + output_layer
                input_operation=graph.get_operation_by_name(input_name)
                output_operation=graph.get_operation_by_name(output_name)

                with tf.Session(config=config, graph=graph) as sess:
                    for t in t_list:
                        results.append(sess.run(output_operation.outputs[0],
                                                {input_operation.outputs[0]: t})
                                       )
            t_list=list()

    for r in results:
        tmp=np.squeeze(r)
        yhat=int(labels[np.argmax(tmp)])
        value_list.append(yhat)
    for i in range(num):
        f=files['file'][i]
        key_list.append(f[0:(len(f) - 5)])
    top_dict=dict(zip(key_list, value_list))
    dict_list.append(top_dict)  # temp fix
    print(len(dict_list[0]))
    cal_accuracy(files, dict_list)
    print("FINISH ", datetime.now())
