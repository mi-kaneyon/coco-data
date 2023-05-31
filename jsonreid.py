import json

# Load the annotations
with open('./cup/test/cup.json', 'r') as f:
    annotations = json.load(f)

# Create a mapping from old category_id to new category_id
category_id_mapping = {16: 1, 18: 2, 3: 3}

# Update category_id in 'categories'
for category in annotations['categories']:
    if category['id'] in category_id_mapping:
        category['id'] = category_id_mapping[category['id']]

# Update category_id in 'annotations'
for annotation in annotations['annotations']:
    if annotation['category_id'] in category_id_mapping:
        annotation['category_id'] = category_id_mapping[annotation['category_id']]

# Save the updated annotations
with open('./cup/test/cupa.json', 'w') as f:
    json.dump(annotations, f)
