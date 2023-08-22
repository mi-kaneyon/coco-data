# coco-data

## Update
- coco format corrector coco_structure_correction.py uploaded.
- coco_checks ：coco format elements checker.

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

# command line for adjust_json_paths.py  
```

python adjust_json_paths.py ./"input path"/"input".json ./"output path"/"output".json ./"root folder"/  

```
## extraid_remove.py
- If you want to remove extra id from json file, please  change in the code path.
```
python extraid_remove.py

```

# coco-corrector (NEW!)
## This sub repository for MMdetection implementation
## Jupyter notebook base coco annotator export file optimizwer.
- Generate coco format json file which is optimized for MMddetection.
- It is convert and check suits
- jupyter notebook file is converter and checker.
- coco_separator.py is file separator for training.

## coco format correction tools
- coco_structure_correction.py: if you cannot train, check your json file structure.

# coco_correctionv2.py
- correction coco format json file which is exported from coco annotator
- At the same time, generate train and val directory with train.json and val json
- coco annotatorからExportしたファイルの適正化とファイルの自動振り分け＋json separate

## Usage
1. End of code is setting area, You can modify your environment.

```
python coco_correctionv2.py

```

## JP
- 日本語説明文はサブフォルダのJPのついたものをご覧ください。
- 英語無くても十分使えるような造りではあります。


