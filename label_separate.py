import os
import pandas as pd
from shutil import copyfile

def label_5(resize):
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_5\\"
    suffix = ".jpeg"
    df = pd.read_csv('trainLabels.csv')
    count = 0
    label = df.level

    for i in range(label.shape[0]):
        src = resize + df.image[i] + suffix
        dst = label_resize + str(label[i]) + "\\" + df.image[i] + suffix
        try:
            copyfile(src, dst)
            count+=1
            if count%200==0:
                print("Done {0}".format(count))
        except Exception:
            pass
        
def label_2(resize):
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2\\"
    suffix = ".jpeg"
    df = pd.read_csv('trainLabels.csv')
    count = 0

    label = df.level

    for i in range(label.shape[0]):
        src = resize + df.image[i] + suffix
        l = int(label[i]!=0)
        dst = label_resize + str(l) + "\\" + df.image[i] + suffix
        try:
            copyfile(src, dst)
            count+=1
            if count%200==0:
                print("Done {0}".format(count))
        except Exception:
            pass
        
def label_2_left_right(resize):
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\"
    left = "left\\"
    right = "right\\"
    suffix = ".jpeg"
    df = pd.read_csv('trainLabels.csv')

    label = df.level
    count = 0
    for i in range(label.shape[0]):
        src = resize + df.image[i] + suffix
        l = int(label[i]!=0)
        is_left = int('left' in src)
        if is_left:
            dst = label_resize + left + str(l) + "\\" + df.image[i] + suffix
        else:
            dst = label_resize + right + str(l) + "\\" + df.image[i] + suffix
        try:
            copyfile(src, dst)
            count+=1
            if count%200==0:
                print("Done {0}".format(count))
        except Exception:
            pass

        
if __name__ == '__main__':
    input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\resize\\"
    #input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\working\\"
    #input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\green\\"
    label_2_left_right(input_path)
    #label_2(input_path)
    #label_5(input_path)
        