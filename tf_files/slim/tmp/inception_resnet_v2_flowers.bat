cd ..
SET DATASET_DIR="./tmp/data/flowers"
SET TRAIN_DIR="./tmp/models/inception_resnet_v2"
SET CHECKPOINT_PATH="./tmp/models/inception_resnet_v2/inception_resnet_v2_2016_08_30.ckpt"

python train_image_classifier.py ^
    --train_dir=%TRAIN_DIR% ^
    --dataset_dir=%DATASET_DIR% ^
    --dataset_name=flowers ^
    --dataset_split_name=train ^
    --model_name=inception_resnet_v2 ^
    --checkpoint_path=%CHECKPOINT_PATH% ^
    --checkpoint_exclude_scopes=InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits ^
    --trainable_scopes=InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits ^
    --max_number_of_steps=50 ^
    --batch_size=32^
    --clone_on_cpu=True
    
cd tmp
    
    