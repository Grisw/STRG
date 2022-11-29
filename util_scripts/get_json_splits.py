import csv
import os
import json

data = {}

classes = os.listdir('data/frames')
with open('data/splits/train_data_id.csv', 'r') as f:
    reader = csv.DictReader(f)
    for item in reader:
        data[item['id']] = {
            "subset": "training",
            "annotations": {
                "label": item['activity'],
                "video_id": item['id'],
                "segment": [1, len(os.listdir(os.path.join('data/frames', item['activity'], item['id'])))]
            }
        }

with open('data/splits/valid_data_id.csv', 'r') as f:
    reader = csv.DictReader(f)
    for item in reader:
        data[item['id']] = {
            "subset": "validation",
            "annotations": {
                "label": item['activity'],
                "video_id": item['id'],
                "segment": [1, len(os.listdir(os.path.join('data/frames', item['activity'], item['id'])))]
            }
        }

with open('data/splits/test_data_id.csv', 'r') as f:
    reader = csv.DictReader(f)
    for item in reader:
        data[item['id']] = {
            "subset": "test",
            "annotations": {
                "label": item['activity'],
                "video_id": item['id'],
                "segment": [1, len(os.listdir(os.path.join('data/frames', item['activity'], item['id'])))]
            }
        }

print('classes', len(classes))
with open('data/data.json', 'w') as f:
    json.dump({
        "labels": classes,
        "database": data}, f)
