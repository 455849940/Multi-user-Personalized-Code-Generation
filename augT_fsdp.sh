export NCCL_P2P_DISABLE=1
CUDA_VISIBLE_DEVICES=1,2,3,5 torchrun --master_port=65532 --nproc_per_node 4 main.py \
    --do_train True \
    --do_eval True \
    --debug_mode False\
    --learning_rate 1e-5\
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 3 \
    --num_train_epochs 20 \
    --choose_model_name perfer_AugT\
    --output_dir augT_model_linear_part \
    --train_data_path ./data/Java_part_programming50/Java_programming_train.json \
    --eval_data_path ./data/Java_part_programming50/Java_programming_dev.json \
    --continue_train False \
    --enable_contrast True \
    --alpha 0.5