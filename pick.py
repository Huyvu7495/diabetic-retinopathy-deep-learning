import os
import numpy as np
from shutil import copyfile
 
def pick(path, n):
    output = "D:\\00_work\\data\\kaggle datasets\\DR\\working\\"
    file_list = os.listdir(path)
    picked = np.random.choice(file_list, n, replace=False)
    
    count = 0
    
    for i in picked:
        src = path + i 
        dst = output + i 
        copyfile(src, dst)
        count+=1
        if count%200 == 0:
            print("Done {0}/{1}".format(count, n))
            
def test_pick(path, n):
    output = "D:\\00_work\\data\\kaggle datasets\\DR\\working\\"
    file_list = os.listdir(path)
    file_list = [f for f in file_list if 'neg' not in f and 'pos' not in f]
    picked = np.random.choice(file_list, n, replace=False)
    
    count = 0
    
    for i in picked:
        src = path + i 
        dst = output + i 
        copyfile(src, dst)
        count+=1
        if count%200 == 0:
            print("Done {0}/{1}".format(count, n))
        
if __name__ == '__main__':
    #path = "D:\\00_work\\data\\kaggle datasets\\DR\\resize\\"
    #path = "D:\\00_work\\data\\kaggle datasets\\DR\\train\\"
    
    path = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\left\\0\\"
    test_pick(path, 250)
    #pick(path, 250)