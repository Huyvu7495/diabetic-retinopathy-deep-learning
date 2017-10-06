# diabetic-retinopathy-deep-learning
Classify Diabetic Retinopathy phases using Deep Learning

**Basic Workflow:**

0. Copy raw train data to ./train/. Remove unused image (e.g. remove level 0 images)

1. Modify line 23 and 24 in pick.py to copy random images from ./train to ./working
2. Open bash Ubuntu. Run ./resize.sh to resize and preprocess all images in ./working, outputs are in ./resize
3. Modify and Use label_separate.py to copy images in to correct label's folder (outputs in ./labeled_xxx).
     **For level 1-4, remove folder 0**
    
4. Goto model in ./tf_files, train models (these folders are from tensorflow for poets)
