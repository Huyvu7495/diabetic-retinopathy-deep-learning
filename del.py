from os import listdir, system
from numpy import random
import re

def del_remain(path):
    files = listdir(path)
    remains = 250
    num_to_del = len(files) - remains
    dels = random.choice(files, num_to_del, replace=False)
    for d in dels:
        print("Del {0}".format(path+d))
        system('del "{0}"'.format(path+d))


def del_all(path):
    files = listdir(path)
    # dels = [f for f in files if re.search('[0-9]', f[0])]
    dels = [f for f in files if re.search('s.*_.*_(ah|ag|ab|ac)', f)]
    # print(len(dels))
    # print(dels)
    # input()
    for d in dels:
        print("Del {0}".format(path+d))
        system('del "{0}"'.format(path+d))



if __name__ == '__main__':
    # path = "D:\\00_work\\data\\kaggle datasets\\DR\\test\\1\\"
    path = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\left\\1\\"
    del_all(path)