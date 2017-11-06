cd ..

SET DATASET_DIR="tmp/data/flowers"
SET TRAIN_DIR="./tmp/models/inception_resnet_v2"
SET CHECKPOINT_DIR="./tmp/models/inception_resnet_v2"
SET CHECKPOINT_FILE="%CHECKPOINT_DIR%/model.ckpt-50.data-00000-of-00001"

python eval_image_classifier.py ^
    --alsologtostderr ^
    --checkpoint_path=%CHECKPOINT_DIR% ^
    --dataset_dir=%DATASET_DIR% ^
    --dataset_name=flowers ^
    --dataset_split_name=validation ^
    --model_name=inception_resnet_v2
    
cd tmp