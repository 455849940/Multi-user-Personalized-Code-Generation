CUDA_VISIBLE_DEVICES=4 python predict.py \
    --debug_mode False \
    --learning_rate 1e-4 \
    --per_device_test_batch_size 2 \
    --output_dir part_model \
    --predict_dirs  ./out_predict/result_part_model_linear.json
