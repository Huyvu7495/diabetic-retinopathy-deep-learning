@echo OFF
SET ARCHITECTURE="inception_v3"

python -m scripts.retrain --bottleneck_dir=tf_files\\bottlenecks ^
--how_many_training_steps=20000 ^
--learning_rate=0.005 ^
--train_batch_size=16 ^
--validation_batch_size=-1 ^
--validation_percentage=3 ^
--test_batch_size=-1 ^
--testing_percentage=5 ^
--eval_step_interval=200 ^
--model_dir=tf_files\\models/"%ARCHITECTURE%" ^
--summaries_dir=tf_files\\training_summaries/"%ARCHITECTURE%" ^
--output_graph=tf_files\\retrained_graph.pb ^
--output_labels=tf_files\\retrained_labels.txt ^
--architecture="%ARCHITECTURE%" ^
--image_dir="D:\\00_work\\data\\kaggle datasets\\DR\\labeled_2_left_right\\left\\"

REM D:\00_work\data\kaggle datasets\DR\labeled_2_left_right\\left
REM D:\00_work\data\kaggle datasets\DR\\labeled_2\\
REM --intermediate_store_frequency=1000 ^
REM --intermediate_output_graphs_dir=tf_files\\intermediate_graph ^