cd ..
SET DATASET_DIR="./tmp/data/flowers"
SET TRAIN_DIR="./tmp/models/inception_v3"
SET CHECKPOINT_PATH="./tmp/models/inception_v3/inception_v3.ckpt"

python train_image_classifier.py ^
    --train_dir=%TRAIN_DIR% ^
    --dataset_dir=%DATASET_DIR% ^
    --dataset_name=flowers ^
    --dataset_split_name=train ^
    --model_name=inception_v3 ^
    --checkpoint_path=%CHECKPOINT_PATH% ^
    --checkpoint_exclude_scopes=InceptionV3/Logits,InceptionV3/AuxLogits ^
    --trainable_scopes=InceptionV3/Logits,InceptionV3/AuxLogits ^
    --max_number_of_steps=50 ^
    --batch_size=32^
    --clone_on_cpu=True
    
cd tmp
    
    