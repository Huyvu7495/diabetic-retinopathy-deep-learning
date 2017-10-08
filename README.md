# diabetic-retinopathy-deep-learning
Classify Diabetic Retinopathy phases using Deep Learning

## Changelog
- New model: ReLU + softmax (in new_retrain.py)
- Early stopping strategy
- Threshold in final softmax layer

## Basic Workflow

1. Copy raw train data to ./train/. Remove unused image (e.g. remove level 0 images)
2. Modify line 23 and 24 in pick.py to copy random images from ./train to ./working
3. Open bash Ubuntu. Run ./resize.sh to resize and preprocess all images in ./working, outputs are in ./resize
4. Modify and Use label_separate.py to copy images in to correct label's folder (outputs in ./labeled_xxx). **For level 1-4, remove folder 0**   
5. Goto model in ./tf_files, train models (these folders are from tensorflow for poets)

## About models
There are 2 new models based on the pre-trained
1. Add a softmax layer (default by tensorflow for poet): retrain.py 
2. Add a ReLU and a softmax layer: new_retrain.py
