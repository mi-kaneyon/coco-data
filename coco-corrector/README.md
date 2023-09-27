# coco-MMoptimize.ipynb

## coco_correctionv2.py
### coco json file separate properly and generate json file tool
- you can modify your coco json file as actual path

'''
python coco_correctionv2.py

'''


'''

# path setting
input_file = 'cup.json'
train_output = 'cup/train/train.json'
val_output = 'cup/val/val.json'
image_dir = 'cup'

'''

## coco annotator generated coco format file optimizer
- It is working on the Jupyter notebook
- It has json file correction and check first file setting well.

  # Easy convert and check image example 


  ![checkResult](https://github.com/mi-kaneyon/coco-data/blob/main/coco-corrector/senchople.png)


# update(1st Aug 2023)
- simple CLI command version is released.
- no sample image display, convert file data only.

# Add adv 
- It is able to check image path
- converting image actual path from coco annotator path.
