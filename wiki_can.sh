export CUDA_VISIBLE_DEVICES=0
python main.py \
--epoch 25 \
--learning_rate .0001 \
--beta 0.5 \
--batch_size 35 \
--sample_size 72 \
--input_height 128 \
--output_height 128 \
--lambda_val 1.0 \
--smoothing 1.0 \
--use_resize True \
--dataset wikiart \
--input_fname_pattern */*.jpg \
--crop False \
--visualize False \
--use_s3 False \
--can True \
--checkpoint_dir logs/dataset=wikiart\,isCan=True\,lr=0.0001\,imsize=128\,batch_size=35/003/checkpoint