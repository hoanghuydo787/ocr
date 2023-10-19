./preprocess.sh /dataset/images/ /dataset/tmp/
python3 predict.py --model /dataset/model/ --data /dataset/tmp/ --output /dataset/output/predict.json --device -1
rm /dataset/tmp/*