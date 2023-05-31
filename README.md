# coco-data

## json file generated coco annotator file convert and check suits.

1. adjust_json_paths.py coco file separater from json file which is exported by coco annotator for actual folder file saving information
coco annotator export whole project data.
If you create data set tree below. you may face the error.
To eliminate training failure, checking actual folder tree and json file modify
exported json file include (a,b,c all annotation result)

Data
|- train
|     |-a.jpg
|     |-b.jpg
|----val
|     |-c.jpg
|- test
2. jsoncheck.py is check the json file id and id name information 
3. jsonreid.py  is changing json file id as you like to optimize object detection accuracy.

All file you can change target in the code. you can realize above function.
