import json
import shutil
import os

def convert_and_separate(input_file, image_dir, train_output, val_output, train_image_dir, val_image_dir, train_ratio=0.8):
    with open(input_file, 'r') as f:
        data = json.load(f)

    images = []
    annotations = []
    for i, item in enumerate(data['items']):
        img_data = {
            'id': i,
            'file_name': os.path.basename(item['file_name']),
            'height': item['height'],
            'width': item['width']
        }
        images.append(img_data)

        for ann in item['annotations']:
            ann_data = {
                'id': len(annotations),
                'image_id': i,
                'bbox': ann['bbox'],
                'category_id': ann['category_id'],
                'segmentation': ann['segmentation'],
                'area': ann['area'],
                'iscrowd': 0,
            }
            annotations.append(ann_data)

    categories = [{'id': i, 'name': name} for i, name in enumerate(data['categories'])]

    train_size = int(len(images) * train_ratio)
    train_images = images[:train_size]
    val_images = images[train_size:]

    train_annotations = [ann for ann in annotations if ann['image_id'] in [img['id'] for img in train_images]]
    val_annotations = [ann for ann in annotations if ann['image_id'] in [img['id'] for img in val_images]]

    train_data = {
        'images': train_images,
        'annotations': train_annotations,
        'categories': categories
    }

    val_data = {
        'images': val_images,
        'annotations': val_annotations,
        'categories': categories
    }

    # Move or copy images to train and val directories
    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(val_image_dir, exist_ok=True)
    for img in train_images:
        shutil.copy(os.path.join(image_dir, img['file_name']), train_image_dir)
    for img in val_images:
        shutil.copy(os.path.join(image_dir, img['file_name']), val_image_dir)

    with open(train_output, 'w') as f:
        json.dump(train_data, f)

    with open(val_output, 'w') as f:
        json.dump(val_data, f)

image_dir = 'cup4' # すべての画像ファイルが格納されているディレクトリ
input_file = 'cup.json'
train_output = 'train.json'
val_output = 'val.json'
train_image_dir = 'cup/train' # トレーニングデータのディレクトリのパス
val_image_dir = 'cup/val' # バリデーションデータのディレクトリのパス
convert_and_separate(input_file, image_dir, train_output, val_output, train_image_dir, val_image_dir)
