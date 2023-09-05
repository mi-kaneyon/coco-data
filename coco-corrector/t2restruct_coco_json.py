
import json
import os

def reformat_coco_json(input_json_path, output_json_path):
    with open(input_json_path, 'r') as f:
        data = json.load(f)

    images = []
    annotations = []
    categories = []

    # Reformat 'images'
    for img in data['images']:
        images.append({
            'file_name': img['file_name'],
            'height': img['height'],
            'width': img['width'],
            'id': img['id']
        })

    # Reformat 'annotations'
    for ann in data['annotations']:
        annotations.append({
            'segmentation': ann.get('segmentation', []),
            'area': ann.get('area', 0),
            'iscrowd': ann.get('iscrowd', 0),
            'image_id': ann['image_id'],
            'bbox': ann['bbox'],
            'category_id': ann['category_id'],
            'id': ann['id']
        })

    # Reformat 'categories'
    for cat in data['categories']:
        categories.append({
            'id': cat['id'],
            'name': cat['name']
        })

    # Combine into a single dictionary
    formatted_data = {
        'images': images,
        'annotations': annotations,
        'categories': categories
    }

    # Save as a new JSON file
    with open(output_json_path, 'w') as f:
        json.dump(formatted_data, f, indent=4)

if __name__ == "__main__":
    # Example usage:
    input_json_path = 'path/to/your/original_annotation.json'
    output_json_path = 'path/to/your/formatted_annotation.json'

    reformat_coco_json(input_json_path, output_json_path)
