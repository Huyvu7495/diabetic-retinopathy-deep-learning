1) Folder structure:
- SETUP
    - log   
        contains generated log when training, testing, and a demo training log for sample dataset
        
    - output    
        contains the final model, label file and training graph for tensorboard
        
    - scripts
        scripts for predict an image, train new model and test a model
        
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
    Report file
    
- REF
    References 
    
    
1) Dataset note:
The train and test dataset provided in this CD is some samples from the full dataset, only sample dataset included in the CD due to size limitation. Download link for full train and test dataset is given in SOURCE/dataset/download_link.txt
After download, extract and override the sample dataset.

2) Setup model prediction process:
- Install Ubuntu 16.04 LTS version (Official installation guide: https://help.ubuntu.com/lts/installation-guide/index.html)

- Copy SETUP and SOURCE to your local folder, the result folder structure should be like this:
    - LOCAL
        - SETUP
        - SOURCE

- Install Python 3.5.2, tensorflow 1.3.0, numpy 1.13.3 (installation guides are located in SOFT) to use the model to predict class of an image in test dataset

3) To predict class of single image:
