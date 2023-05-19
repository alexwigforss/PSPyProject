# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html
# Som referens hur man kan trimma bort bakgrundsfärg
import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('sample4.jpg',0)
# img = cv2.imread('92201_3.webp',0)
img = cv2.imread('92201_3.webp',0)

ret,thresh1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,110,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)

titles = ['Original Image','100','110','120']
images = [img, thresh1, thresh2, thresh3]

# Filename
filename = 'savedImage'
ext = '.jpg'

# Using cv2.imwrite() method
# Saving the image
i = 0
for e in images:
    cv2.imwrite(str(i) + titles[i] + ext, e)
    i += 1

# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()