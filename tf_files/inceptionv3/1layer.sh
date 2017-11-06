
ARCHITECTURE="inception_v3"

python3 -m scripts.retrain_1 --bottleneck_dir=tf_files/bottlenecks \
--how_many_training_steps=50000 \
--learning_rate=0.001 \
--train_batch_size=16 \
--validation_batch_size=-1 \
--validation_percentage=3 \
--test_batch_size=-1 \
--testing_percentage=5 \
--eval_step_interval=1000 \
--model_dir=tf_files/models/"${ARCHITECTURE}" \
--summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
--output_graph=tf_files/classifier_1.pb \
--output_labels=tf_files/label_1.txt \
--architecture="${ARCHITECTURE}" \
--image_dir="/mnt/d/00_work/data/kaggle datasets/DR/labeled_2/"


