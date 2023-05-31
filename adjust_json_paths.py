import os
import json
import argparse

def adjust_paths_in_json(input_json, output_json, root_directory):
    with open(input_json) as f:
        data = json.load(f)

    # Initialize an empty list to keep track of images that exist
    valid_images = []

    for img in data['images']:
        img_file = img['file_name']
        if os.path.exists(os.path.join(root_directory, img_file)):
            valid_images.append(img)
        else:
            print(f"File {img_file} does not exist in directory {root_directory}.")

    # Replace the 'images' field in the data with the valid images
    data['images'] = valid_images

    with open(output_json, 'w') as f:
        json.dump(data, f)

def parse_args():
    parser = argparse.ArgumentParser(description="Adjust paths in JSON file.")
    parser.add_argument('input_json', help='input json file')
    parser.add_argument('output_json', help='output json file')
    parser.add_argument('root_directory', help='root directory of data')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    adjust_paths_in_json(args.input_json, args.output_json, args.root_directory)
