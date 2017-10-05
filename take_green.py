import os
import numpy as np
import cv2
from multiprocessing import Process

def pick(path):
    output = "D:\\00_work\\data\\kaggle datasets\\DR\\green\\"
    file_list = os.listdir(path)
    num = len(file_list)
    file_list1 = file_list[0:num//2]
    file_list2 = file_list[num//2:num]
    
    p1 = Process(target=fork, args = ('P1', file_list1, output, path))
    p2 = Process(target=fork, args = ('P2', file_list2, output, path))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
#    for f in file_list:
#        image=cv2.imread(path+f)
#        image[:,:,[0,2]] = 0
#        cv2.imwrite(output+f,image)
#        count+=1
#        if count%200 == 0:
#            print("Done {0}/{1}".format(count, len(file_list)))
            
def fork(name, file_list, output, path):
    print("{0} started".format(name))
    count = 0
    num = len(file_list)
    for f in file_list:
        src = path + f 
        dst = output + f 
        green(src, dst)
        count+=1
        if count%200 == 0:
            print("{0} Done {1}/{2}".format(name, count, num))
    print("{0} end".format(name))
    
def green(src, dst):
    image=cv2.imread(src)
    image[:,:,[0,2]] = 0
    #image[:,:,1] = (image[:,:,1] - np.mean(image[:,:,1]))/(np.max(image[:,:,1]) - np.min(image[:,:,1]))
    cv2.imwrite(dst,image)
    
if __name__ == '__main__':
    path = "D:\\00_work\\data\\kaggle datasets\\DR\\resize\\"
    #path = "D:\\00_work\\data\\kaggle datasets\\DR\\working\\"
    pick(path)