from pycocotools.coco import COCO
import requests

# instantiate COCO specifying the annotations json path
coco = COCO('instances_train2014.json')
# Specify a list of category names of interest
catIds = coco.getCatIds(catNms=['person'])
# Get the corresponding image ids and images using loadImgs
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)

# Save the images into a local folder
cpt = 0

for im in images:
    if (cpt < 4000):
        img_data = requests.get(im['coco_url']).content
        with open('Sohas_weapon-Detection_enhanced/coco_person/' + im['file_name'], 'wb') as handler:
            handler.write(img_data)
            cpt = cpt+1
    else: print('Finish')