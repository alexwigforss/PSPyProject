# https://www.scrapingbee.com/blog/download-image-python/
import requests
import shutil
import cv2
import numpy as np
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

from main import test_images as ti

def downloadImgs():
    if not os.path.exists('./bilder'):
        os.makedirs('./bilder')
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
list_of_fnames = []
def getPaths():
    global list_of_paths
    rpath = os.getcwd() + '\\' + 'bilder'
    content = os.listdir(rpath)
    for e in content:
        if os.path.isfile(os.getcwd() + '\\bilder\\' + e):
            list_of_paths.append(os.getcwd() + '\\bilder\\' + e)
            list_of_fnames.append(e.replace('jpg','txt'))
getPaths()

def getTxtFileNames():
    global list_of_paths
    result = []
    rpath = os.getcwd() + '\\' + 'text'
    for e in os.listdir(rpath):
        if os.path.isfile(os.getcwd() + '\\text\\' + e):
            # list_of_paths.append(os.getcwd() + '\\bilder\\' + e)
            result.append(e)
    return result

# https://jdhao.github.io/2019/09/11/opencv_unicode_image_path/
def prepOcr(path):
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8),
                   cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh, rect_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
    im2 = img.copy()
    return contours,im2


# # A text file is created and flushed
def createOrFlushFile(fname):
    file = open('./text/'+fname, "w+",encoding='utf8')
    file.write("")
    file.close()

def getChars(contours, im2, filename):
    # createOrFlushFile(filename) # Uncoment to empty files before writing
    file = open('./text/'+filename, "a",encoding='utf8')
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
    # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
    # Open the file in append mode
     
    # Apply OCR on the cropped image
        text = pytesseract.image_to_string(cropped)
        # https://pyimagesearch.com/2020/08/03/tesseract-ocr-for-non-english-languages/
        # text = pytesseract.image_to_string(cropped,lang = 'swe')
        if len(text) > 5:
            print(len(text),text)
            # Appending the text into file
            file.write(text.replace('\n', ' '))
            file.write("\n")
     
    # Close the file
    file.close

if __name__ == '__main__':
    if not os.path.exists('./text'):
        os.makedirs('./text')

    # Teckenavläsning
    for e in enumerate(list_of_paths):
        contours, im2 = prepOcr(e[1])
        getChars(contours, im2, list_of_fnames[e[0]])

# [ ] Classinmatning

"""
TBD
[x] Om katalog inte finns skapa
[x] Katalog för texten också, sparas nu i roten.
"""
#paths = ['bilder/Höstmorot_9396_3.jpg','bilder/Kålrot_92201_3.jpg']
#contours, im2 = prepOcr(list_of_paths[0])
#getChars(contours, im2, 'filename.txt')