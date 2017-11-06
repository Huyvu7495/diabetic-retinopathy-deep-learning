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
from scripts.label_image import *
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
    for i in range(num):
        f = files['file'][i]
        d = files['dir'][i]
        idx = f[0:len(f) - 5]
        predict_list = list()

        # correct = int(df[df.image == idx].level.values > 0)
        correct = int(d)
        for d in dict_list:
            predict_list.append(d[idx])
        predict = max_count(predict_list)
        if predict == 1:
            if predict == correct:
                TP += 1
            else:
                miss_class.append(correct)
                FP += 1
        else:
            if predict == correct:
                TN += 1
            else:
                miss_class.append(correct)
                FN += 1

    print(predict_list)
    print(predict, correct)

    try:
        P = TP / (TP + FP)
        R = TP / (TP + FN)
        F1 = (2 * P * R) / (P + R)
        ACC = (TP + TN) / (TP + TN + FP + FN)
    except ZeroDivisionError:
        P = 0
        R = 0
        F1 = 0
    print(miss_class)
    print(TP, FP, TN, FN)
    print('CORRECT \t{0}/{1}'.format(TP + TN, num))
    print("PRECISION \t{0}".format(P))
    print("RECALL \t\t{0}".format(R))
    print("F1 \t\t{0}".format(F1))
    print("ACC \t\t{0}".format(ACC))


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
    if args.threshold:
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

    graph_list = ['tf_files/classifier_1.pb',
                'tf_files/classifier_2.pb',
                'tf_files/classifier_3.pb']

    label_list = ['tf_files/label_1.txt',
                'tf_files/label_2.txt',
                'tf_files/label_3.txt']
    # graph_list = ['tf_files/classifier_2.pb']
    # label_list = ['tf_files/label_2.txt']
    print(label_file, model_file)
    # root_path = PROJECT_PATH + 'working/'
    root_path = PROJECT_PATH + 'test/'
    dir_list = listdir(root_path)
    files = {'file': list(),
             'dir': list()}

    for d in dir_list:
        tmp = listdir(root_path + d)

        for i in tmp:
            files['file'].append(i)
            files['dir'].append(d)

    num = len(files['dir'])
    dict_list = list()
    count = 0

    print("BEGIN ", datetime.now())

    t_list = list()
    key_list = []
    for i in range(num):
        f = files['file'][i]
        d = files['dir'][i]
        src = root_path + d + '/' + f
        key_list.append(f[0:(len(f) - 5)])
        t_list.append(read_tensor_from_image_file(src,
                                                  input_height=input_height,
                                                  input_width=input_width,
                                                  input_mean=input_mean,
                                                  input_std=input_std)
                      )
        count += 1
        if count % 20 == 0:
            print("READ {0}/{1}".format(count, num))

    print("CALCULATING ", datetime.now())
    for model_idx in range(len(graph_list)):
        print(graph_list[model_idx], label_list[model_idx])

        value_list = list()
        results = list()
        graph = load_graph(graph_list[model_idx])
        labels = load_labels(label_list[model_idx])
        input_name = "import/" + input_layer
        output_name = "import/" + output_layer
        input_operation = graph.get_operation_by_name(input_name)
        output_operation = graph.get_operation_by_name(output_name)

        with tf.Session(config=config, graph=graph) as sess:
            for t in t_list:
                results.append(sess.run(output_operation.outputs[0],
                                        {input_operation.outputs[0]: t})
                               )

            for r in results:
                tmp = np.squeeze(r)
                yhat = int(labels[np.argmax(tmp)])
                value_list.append(yhat)

        top_dict = dict(zip(key_list, value_list))
        dict_list.append(top_dict)

    cal_accuracy(files, dict_list)
    print("FINISH ", datetime.now())
