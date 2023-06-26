import json

# Load the annotations
with open('./cup/train/cupa.json', 'r') as f:
    annotations = json.load(f)

# Update category_id in 'annotations'
new_annotations = []

for annotation in annotations['annotations']:
    if annotation['category_id'] != 19:
        new_annotations.append(annotation)

# Replace the old annotations with the new ones
annotations['annotations'] = new_annotations

# Save the updated annotations
with open('./cup/train/cupa.json', 'w') as f:
    json.dump(annotations, f)
