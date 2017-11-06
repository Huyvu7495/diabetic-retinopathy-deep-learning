cd ..

DATASET_DIR=/mnt/d/00_work/data/kaggle\ datasets/DR/labeled_2_left_right/
TRAIN_DIR="./tmp/models/dr_inception_resnet_v2"
CHECKPOINT_PATH="./tmp/models/dr_inception_resnet_v2"

python3 eval_image_classifier.py  \
    --alsologtostderr  \
    --checkpoint_path="${CHECKPOINT_DIR}"  \
    --dataset_dir="${DATASET_DIR}"  \
    --dataset_name=dr  \
    --dataset_split_name=validation  \
    --model_name=inception_resnet_v2
    
cd tmp