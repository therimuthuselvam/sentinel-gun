# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 01:05:40 2019

@author: Ragavan Rana
"""

import numpy as np
import cv2

img = cv2.imread('theri.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('therigray.png',img)
    cv2.destroyAllWindows()