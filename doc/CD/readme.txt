1) Folder structure:
- SETUP
    - log   
        contains generated log when training, testing, and a demo training log for sample dataset
        
    - output    
        contains the final model, label file and training graph for tensorboard
        
    - scripts
        scripts for predict an image, train new model and evaluate model
        
    - tf_files
        contains base inception-v3 model
    
- SOURCE 
    - dataset 
        sample train and test dataset, onedrive download link for full dataset.
        
    - python 
        source code in Python 3.5.2 for training and testing model, tensorflow library.
        
- SOFT
    How to install these tools
        - imagemagick
        - numpy
        - parallel
        - tensorflow

- BAO CAO 
    Report files
    
- REF
    References 
    

1) Basic Setup:
- Install Ubuntu 16.04 LTS version (Official installation guide: https://help.ubuntu.com/lts/installation-guide/index.html)
- Copy SETUP and SOURCE to your local folder, the result folder structure should be like this:
    - LOCAL
        - SETUP
        - SOURCE
- Install Python 3.5.2, tensorflow 1.3.0, numpy 1.13.3 (installation guides are located in SOFT) to use the model to predict class of an image in test dataset

    
2) Dataset note:
The train and test dataset provided in this CD is some samples from the full dataset, only sample dataset included in the CD due to size limitation. Download location for full train and test dataset is given in SOURCE/dataset/download_link.txt
After download, extract and override the sample dataset.


3) PREDICTION: predict class for a single image (using best model - v3)
- Procedure:
    - Open terminal in Ubuntu
    - Change working directory to SETUP/scripts
    - Execute this line in terminal:
            $ ./predict {0} {1} {2}
        
        With:   {0} is the directory of the image from SOURCE/test
                {1} is the number of the image
                {2} is "left" or "right"
                
                e.g. $ ./predict 2 41675 left
- The output is the possibility of classes

4) TESTING: evaluate model (predict class for all test images to get statistics)
- Heavy task, depends heavily on CPU, RAM and Storage Disk I/O speed
- Procedure:
    - Open terminal in Ubuntu
    - Change working directory to SETUP/scripts
    - Execute this line in terminal:
            $ ./test {0} {1} {2}
        
        With:   {0} is the directory of the image from SOURCE/test
                {1} is the number of the image
                {2} is "left" or "right"
                
                e.g. $ ./test 2 41675 left

5) TRAINING: train a diabetic retinopathy classification model based on inception-v3 model
- Heavy task, depends heavily on CPU, RAM and Storage Disk I/O speed

- Procedure:
    - Open terminal in Ubuntu
    - Change working directory to SETUP/scripts
    - Execute this line in terminal (change version if you want to)
            $ ./train_v3
