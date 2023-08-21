import json

def is_coco_format_valid(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)

        # 必要なキーのチェック
        assert 'images' in data, "'images' key is missing"
        assert 'annotations' in data, "'annotations' key is missing"
        assert 'categories' in data, "'categories' key is missing"

        # 'images'の各要素が必要なキーを持っているかチェック
        for image in data['images']:
            assert 'id' in image, "'id' key is missing in 'images'"
            assert 'file_name' in image, "'file_name' key is missing in 'images'"
            assert 'height' in image, "'height' key is missing in 'images'"
            assert 'width' in image, "'width' key is missing in 'images'"

        # 'annotations'の各要素が必要なキーを持っているかチェック
        for annotation in data['annotations']:
            assert 'id' in annotation, "'id' key is missing in 'annotations'"
            assert 'image_id' in annotation, "'image_id' key is missing in 'annotations'"
            assert 'bbox' in annotation, "'bbox' key is missing in 'annotations'"
            assert 'category_id' in annotation, "'category_id' key is missing in 'annotations'"

        # 'categories'の各要素が必要なキーを持っているかチェック
        for category in data['categories']:
            assert 'id' in category, "'id' key is missing in 'categories'"
            assert 'name' in category, "'name' key is missing in 'categories'"

        print("Correct")
    except AssertionError as e:
        print(f"Error: {str(e)}")
        return False

    return True

# 使用方法
json_file = 'cup/train/train.json'
is_coco_format_valid(json_file)

