1) Folder structure:
- SETUP
    - log   
        contains generated log when training, testing, and a demo training log for sample dataset
        
    - output    
        contains the final model, label file 
        
    - scripts
        scripts for predict an image, train new model and evaluate model
        
    - tf_files
        contains base inception-v3 model
    
- SOURCE 
    - dataset 
        sample train and test dataset, onedrive download link for full dataset.
        
    - preprocess
        sample preprocess scripts
        for reference only, annot re-run due to the lack of raw dataset and preprocess is the most time consuming task
        all of the given datasets are already preprocessed well
        
    - python 
        source code in Python 3.5.2 for training and testing model, tensorflow library.
        
- SOFT
    How to install these tools
        - imagemagick
        - python and libraries
        - parallel
        - tensorflow

- BAO CAO 
    Report files
    
- REF
    References 
    

1) Basic Setup:
- Install Ubuntu 16.04 LTS version (Official installation guide: https://help.ubuntu.com/lts/installation-guide/index.html)
- Copy SETUP and SOURCE to your local folder, the result folder structure should be like this:
    - {LOCAL}
        - SETUP
        - SOURCE
- Install Python 3.5.2, tensorflow 1.3.0, numpy 1.13.3 (installation guides are located in SOFT) to use the model to predict DR stage of an image in test dataset
- Now you can PREDICT, TEST, TRAIN model using sample dataset
    
2) Dataset note:
The train and test dataset provided in this CD is some samples from the full dataset, only sample dataset included in the CD due to size limitation. Download location for full train and test dataset is given in SOURCE/dataset/download_link.txt
After download dataset, extract and override the sample dataset.

3) PREDICTION: predict stage for a single image (using best model - v3)
- Procedure:
    - Open terminal in Ubuntu
    - Change working directory to SETUP/scripts
    - Execute this line in terminal:
            $ ./predict {0} {1} {2}
        
        With:   {0} is the directory of the image from SOURCE/test
                {1} is the number of the image
                {2} is "left" or "right"
                
                e.g. $ ./predict 3 13823 left
- The output is the possibility of stages

4) TESTING: evaluate model (predict for all test images to get statistics)
- Heavy task, depends heavily on CPU, RAM and Storage Disk I/O speed
- Procedure:
    - Open terminal in Ubuntu
    - Change working directory to SETUP/scripts
    - Execute this line in terminal:
            $ ./test_v{0}
            
        With:   {0} is the model version (1 | 2 | 3)

5) TRAINING: train a diabetic retinopathy classification model based on inception-v3 model
- Heavy task, depends heavily on CPU, RAM and Storage Disk I/O speed

- Procedure:
    - Open terminal in Ubuntu
    - Change working directory to SETUP/scripts
    - Execute this line in terminal (if there is only sample dataset)
            $ ./train_demo

    - Execute this line in terminal (if there is full dataset)
            $ ./train_v{0}
            
        With:   {0} is the model version (1 | 2 | 3)
        
    - The recently trained model is SETUP/tf_files/classfier.pb
    - The recently trained label is SETUP/tf_files/label.txt
    
    
        
   
