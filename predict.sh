# ./preprocess.sh /dataset/images/ /dataset/tmp/
python3 predict.py --model /model/ --data /dataset/images/ --output /dataset/output/predict.json --device -1
# rm /dataset/tmp/*