# https://www.scrapingbee.com/blog/download-image-python/
import requests
import shutil
from main import test_images as ti

def downloadImgs():
    for e in ti:
        url = ti[e]
        fname = 'bilder/' + e.split()[0] + '_' + ti[e].split('/')[-1] + '.jpg'
        res = requests.get(url, stream = False)

        if res.status_code == 200:
            with open(fname,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            print('Image sucessfully Downloaded: ',fname)
        else:
            print('Image Couldn\'t be retrieved: ',res.status_code)