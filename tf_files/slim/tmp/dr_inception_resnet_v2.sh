cd ..
DATASET_DIR=/mnt/d/00_work/data/kaggle\ datasets/DR/labeled_2_left_right/
TRAIN_DIR="./tmp/models/dr_inception_resnet_v2"
CHECKPOINT_PATH="./tmp/models/dr_inception_resnet_v2/inception_resnet_v2_2016_08_30.ckpt"

python3 train_image_classifier.py \
    --train_dir="${TRAIN_DIR}" \
    --dataset_dir="${DATASET_DIR}" \
    --dataset_name=dr \
    --dataset_split_name=train \
    --model_name=inception_resnet_v2 \
    --checkpoint_path="${CHECKPOINT_PATH}" \
    --checkpoint_exclude_scopes=InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits \
    --max_number_of_steps=500 \
    --optimizer=momentum \
    --batch_size=32 \
    --clone_on_cpu=True
    
cd tmp
    
    
    #--trainable_scopes=InceptionResnetV2/Logits,InceptionResnetV2/AuxLogits 