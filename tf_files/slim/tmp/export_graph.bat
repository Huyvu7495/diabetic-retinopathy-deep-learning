cd ..
python export_inference_graph.py ^
  --alsologtostderr ^
  --model_name=inception_resnet_v2 ^
  --output_file=./tmp/inception_resnet_v2_inf_graph.pb
cd tmp