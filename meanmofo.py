import cv2
import numpy as np
import sys
from os import listdir
from os.path import isfile, join
from multiprocessing import Process, Queue
import math

def mean(path, onlyfiles, out_q):
    img1 = cv2.imread(join(path, onlyfiles[0]))
    b_sum, g_sum, r_sum = cv2.split(img1)
    n_sum = img1.size / 3

    for n in range(1, len(onlyfiles)):
      img = cv2.imread(join(path, onlyfiles[n]))
      b, g, r = cv2.split(img)
      b_sum += b
      g_sum += g
      r_sum += r
      n = img.size / 3 #number of pixel each channel
      n_sum += n
    out_q.put(b_sum)
    out_q.put(g_sum)
    out_q.put(r_sum)
    out_q.put(n_sum)

def std(path, onlyfiles, out_q, b_mean, g_mean, r_mean, n_sum):
    for n in range(0, len(onlyfiles)):
        img = cv2.imread(join(path, onlyfiles[n]))
        b, g, r = cv2.split(img)
        b_pix = 0.0
        for b_pix in b:
            b_pix = float(np.sum(b_pix))
            b_pix += (b_pix - b_mean) ** 2
        for g_pix in g:
            g_pix = float(np.sum(g_pix))
            g_pix += (g_pix - g_mean) ** 2
        for r_pix in b:
            r_pix = float(np.sum(r_pix))
            r_pix += (r_pix - r_mean) ** 2

    b_std = math.sqrt(b_pix / n_sum)
    g_std = math.sqrt(g_pix / n_sum)
    r_std = math.sqrt(r_pix / n_sum)
    out_q.put(b_std)
    out_q.put(g_std)
    out_q.put(r_std)

def multi(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    onlyfiles1 = onlyfiles[0:len(onlyfiles) // 2]
    onlyfiles2 = onlyfiles[len(onlyfiles) // 2:len(onlyfiles)]

    out_q1 = Queue()
    out_q2 = Queue()

    p1 = Process(target=mean, args=(path, onlyfiles1, out_q1))
    p2 = Process(target=mean, args=(path, onlyfiles2, out_q2))

    p1.start()
    p2.start()

    # b1, g1, r1, n1 = out_q1.get()
    b1 = out_q1.get()
    g1 = out_q1.get()
    r1 = out_q1.get()
    n1 = out_q1.get()
    # b2, g2, r2, n2 = out_q2.get()
    b2 = out_q2.get()
    g2 = out_q2.get()
    r2 = out_q2.get()
    n2 = out_q2.get()

    p1.join()
    p2.join()

    p1.terminate()
    p2.terminate()

    b = b1 + b2
    g = g1 + g2
    r = r1 + r2
    n = n1 + n2

    B_mean = float(np.sum(b)) / n  # convert to float, as B, G, and R will otherwise be int
    G_mean = float(np.sum(g)) / n
    R_mean = float(np.sum(r)) / n

    p1 = Process(target=std, args=(path, onlyfiles1, out_q1, B_mean, G_mean, R_mean, n))
    p2 = Process(target=std, args=(path, onlyfiles2, out_q2, B_mean, G_mean, R_mean, n))

    p1.start()
    p2.start()

    b1 = out_q1.get()
    g1 = out_q1.get()
    r1 = out_q1.get()

    b2 = out_q2.get()
    g2 = out_q2.get()
    r2 = out_q2.get()

    p1.join()
    p2.join()

    B_std= b1 + b2
    G_std = g1 + g2
    R_std = r1 + r2

    text_file = open(path + "/mean_n_std.txt", "w")
    text_file.write("R mean: %s\n" % R_mean)
    text_file.write("B mean: %s\n" % B_mean)
    text_file.write("G mean: %s\n" % G_mean)
    text_file.write("R std: %s\n" % R_std)
    text_file.write("B std: %s\n" % B_std)
    text_file.write("G std: %s\n" % G_std)
    text_file.close()

    print 'R mean:', R_mean
    print 'B mean:', B_mean
    print 'G mean:', G_mean
    print 'R std:', R_std
    print 'B std:', B_std
    print 'G std:', G_std

if __name__ == '__main__':
    # sys.argv[1] = 'E:\UIT\\00-Thesis\\test/'
    mypath = sys.argv[1]
    multi(mypath)