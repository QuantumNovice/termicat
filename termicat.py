import numpy as np
#from PIL import Image
from colr import Colr as C
import cv2
import os
import sys
import time

# def load_image( infilename ) :
#     img = Image.open( infilename )
#     img.load()
#     data = np.asarray( img, dtype="int32" )
#     return data


#image = load_image('test.jpg')


def termicat(img):
    img = cv2.imread(img)
    w,h = os.get_terminal_size()
    sf = min(w,h)
    res = cv2.resize(img, dsize=(sf, sf), interpolation=cv2.INTER_CUBIC)


    for i, pixel_line in enumerate(res):
        str = ''
        for j, (r,g,b) in enumerate(pixel_line):
            str+=C().b_rgb(r,g,b).rgb(0, 0, 0, ' ')
        print(str)

def main():
    t1 = time.time()
    if len(sys.argv)!=0:
        for img in sys.argv[1:]:
            termicat(img)
    else:
        print('termicat [img1 img2 ...]')
    t2 = time.time()
    print(f'Time:{t2-t1}s')

if __name__ == '__main__':
    main()