import json
import pandas as pd


def createLabelList(input_dir):
    #label_input_dir = "D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\"
    suffix = ".jpeg"
    df = pd.read_csv('trainLabels.csv')
    label_dict = {'0': list(), '1': list(), '2': list(),
                  '3': list(), '4': list()}
    label = df.level
    count = 0
    for i in range(label.shape[0]):
        # src = input_dir + df.image[i] + suffix
        src = df.image[i] + suffix
        l = int(label[i])
        label_dict[str(l)].append(src)
        count += 1
        if count % 1000 == 0:
            print("FINISH {0}/{1}".format(count, label.shape[0]))

    with open('labelDictionary.json', 'w') as f:
        json.dump(label_dict, f)


if __name__ == '__main__':
    input_path = "D:\\00_work\\data\\kaggle datasets\\DR\\train\\"
    createLabelList(input_path)
