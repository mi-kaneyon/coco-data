import json

# Load the provided JSON file
with open('provided.json', 'r') as f:
    data = json.load(f)

# Convert 'path' to 'file_name' in 'images'
for image in data['images']:
    image['file_name'] = image.pop('path')

# Remove 'isbbox' from 'annotations'
for annotation in data['annotations']:
    annotation.pop('isbbox', None)

# Remove 'supercategory' and 'color' from 'categories'
for category in data['categories']:
    category.pop('supercategory', None)
    category.pop('color', None)

# Save the converted data to a new JSON file
with open('converted.json', 'w') as f:
    json.dump(data, f)
