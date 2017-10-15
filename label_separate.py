import os
import pandas as pd
from shutil import copyfile
from datetime import datetime
import re

def final_label_5(resize, type='copy'):
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_5\\"
    suffix = ".jpeg"
    df = pd.read_csv('trainLabels.csv')
    count = 0
    num = df.shape[0]
    file_list = os.listdir(resize)
    file_list = [f for f in file_list if not re.search('[0-9]', f[0])]
    
    for f in file_list:
        org_name = re.search('[0-9].*t', f)[0]
        label = df.level[df.image==org_name].values[0]
        src = resize+f
        if type=='copy':
            dst = label_resize + str(label) + "\\" + f
            cmd = 'copy "{0}" "{1}">nul'.format(src, dst)
            
        else:
            dst = label_resize + str(label) + "\\" + f
            cmd = 'move "{0}" "{1}">nul'.format(src, dst)
            
        os.system(cmd)
        count+=1
        if count%200==0:
            print("Done {0}".format(count))
         
def org_label_5(resize):
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
            #cmd = 'move "{0}" "{1}"'.format(src, dst)
            #os.system(cmd)
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
                
def uni_label_2(resize):
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2\\"
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_1-4\\"
    suffix = ".jpeg"
    df = pd.read_csv('trainLabels.csv')
    count = 0

    label = df.level

    for i in range(label.shape[0]):
        src = resize + df.image[i] + suffix
        l = label[i]
        if l!=0 and l!=2:
            dst = label_resize + str(l) + "\\" + df.image[i] + suffix
            try:
                copyfile(src, dst)
                count+=1
                if count%200==0:
                    print("Done {0}".format(count))
            except Exception:
                pass
        
def label_2_left_right(resize):
    #label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\"
    label_resize = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_1-4\\"
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
    input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\train\\"
    #input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\resize\\"
    #input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\working\\"
    #input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\left\\1\\"
    #label_2_left_right(input_path)
    uni_label_2(input_path)
    #final_label_5(input_path)
    #org_label_5(input_path)
        