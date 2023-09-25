import json
import cv2
import matplotlib.pyplot as plt
import os

def display_annotations(json_path, image_dir):
    with open(json_path, 'r') as f:
        data = json.load(f)

    images = data['images']
    annotations = data['annotations']

    image_dict = {}
    for img in images:
        image_dict[img['id']] = os.path.join(image_dir, img['file_name'].split('/')[-1])

    for ann in annotations:
        image_path = image_dict.get(ann['image_id'], None)
        
        if image_path is None:
            print(f"Image ID {ann['image_id']} not found in image dictionary.")
            continue

        print(f"Trying to read image: {image_path}")

        try:
            image = cv2.imread(image_path)
            if image is None:
                print(f"Image {image_path} could not be read.")
                continue
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(f"Image {image_path} not found. Error: {e}")
            continue

        bbox = ann['bbox']
        x, y, w, h = map(int, bbox)

        cv2.rectangle(image, (x, y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow('Annotation Checker', image)

        print("Press 'n' to continue, 'q' to quit.")
        while True:
            key = cv2.waitKey(0)
            if key == ord('n'):
                break
            if key == ord('q'):
                cv2.destroyAllWindows()
                return

# Usage
json_path = "train/train.json"  # change your coco json file and path
image_dir = "train"  # change your image directory
display_annotations(json_path, image_dir)
