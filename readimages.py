# https://www.scrapingbee.com/blog/download-image-python/
import requests
import shutil

from main import test_images as ti

def downloadImgs():
    # Om/bilder inte finns skapa /bilder
    for e in ti:
        url = ti[e]
        fname = 'bilder/' + e.split()[0] + '_' + ti[e].split('/')[-1]
        res = requests.get(url, stream = True)

        if res.status_code == 200:
            with open(fname,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',fname ,e)
        else:
            print('Image Couldn\'t be retrieved: ',res.status_code,e)
# downloadImgs()
import os
list_of_paths = []
def getPaths():
    global list_of_paths
    rpath = os.getcwd() + '\\' + 'bilder'
    content = os.listdir(rpath)
    for e in content:
        if os.path.isfile(os.getcwd() + '\\bilder\\' + e):
            list_of_paths.append(os.getcwd() + '\\bilder\\' + e)
getPaths()

import cv2
import numpy

os.system('cls')
i=0
for e in list_of_paths:
    # Applicera Threshold
    print(e)
    img = cv2.imread(e,0)
    ret,thresh3 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
    # Spara till subkattalog bilder/p
    cv2.imwrite(str(i) + '.jpg', e)
    i += 1


