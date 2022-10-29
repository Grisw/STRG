import os
import json
import tqdm

VALIDATIONS = 0.5

data = {}
classes = os.listdir('data/frames')
for c in tqdm.tqdm(classes):
    class_path = os.path.join('data/frames', c)
    videos = os.listdir(class_path)
    vals = int(len(videos) * VALIDATIONS)
    if vals == 0 or vals == len(videos):
        continue
    for video in videos[:vals]:
        data[video] = {
            "subset": "validation",
            "annotations": {
                "label": c,
                "video_id": video,
                "segment": [1, len(os.listdir(os.path.join(class_path, video)))]
            }
        }
    for video in videos[vals:]:
        data[video] = {
            "subset": "training",
            "annotations": {
                "label": c,
                "video_id": video,
                "segment": [1, len(os.listdir(os.path.join(class_path, video)))]
            }
        }

print('classes', len(classes))
with open('data/data.json', 'w') as f:
    json.dump({
        "labels": classes,
        "database": data}, f)
