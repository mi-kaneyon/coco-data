import json
import pprint
import os

# Load the provided JSON file--here is yourself change to check coco jsonfile.
with open('converted.json', 'r') as f:
    data = json.load(f)

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

# Print an example from the converted data
pprint.pprint(data['images'][0])  # Print the first image
pprint.pprint(data['annotations'][0])  # Print the first annotation
pprint.pprint(data['categories'][0])  # Print the first category

