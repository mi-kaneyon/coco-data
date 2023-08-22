import os
import json
from shutil import copyfile
from random import shuffle

def convert_and_separate(input_file, train_output, val_output, image_dir):
    # ディレクトリが存在しない場合は作成
    train_dir = os.path.dirname(train_output)
    val_dir = os.path.dirname(val_output)
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    # 既存のJSONファイルを読み込む
    with open(input_file, 'r') as f:
        data = json.load(f)

    # 分割比率を設定 (80% トレーニング, 20% 検証)
    split_ratio = 0.8
    num_train = int(split_ratio * len(data['images']))

    # 画像の順序をランダムにシャッフル
    shuffled_images = data['images'].copy()
    shuffle(shuffled_images)

    # トレーニング用と検証用に分割
    train_images = shuffled_images[:num_train]
    val_images = shuffled_images[num_train:]

    # 画像IDをキーとしてアノテーションをマップ
    annotations_map = {}
    for ann in data['annotations']:
        image_id = ann['image_id']
        if image_id not in annotations_map:
            annotations_map[image_id] = []
        annotations_map[image_id].append(ann)

    # トレーニングデータと検証データを作成
    train_data = {
        'images': train_images,
        'annotations': [ann for img in train_images for ann in annotations_map[img['id']]],
        'categories': data['categories']
    }
    val_data = {
        'images': val_images,
        'annotations': [ann for img in val_images for ann in annotations_map[img['id']]],
        'categories': data['categories']
    }

    # トレーニングデータと検証データをJSONファイルに書き込む
    with open(train_output, 'w') as f:
        json.dump(train_data, f)
    with open(val_output, 'w') as f:
        json.dump(val_data, f)

    # 画像ファイルをコピー
    for img in train_images:
        src_path = os.path.join(image_dir, img['file_name'])
        dest_path = os.path.join(train_dir, img['file_name'])
        copyfile(src_path, dest_path)
    for img in val_images:
        src_path = os.path.join(image_dir, img['file_name'])
        dest_path = os.path.join(val_dir, img['file_name'])
        copyfile(src_path, dest_path)

# パスの設定
input_file = 'cup.json'
train_output = 'cup/train/train.json'
val_output = 'cup/val/val.json'
image_dir = 'cup'

convert_and_separate(input_file, train_output, val_output, image_dir)
