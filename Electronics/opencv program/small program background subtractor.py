# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 00:37:13 2019

@author: Theriselvam
"""

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
fgbg = cv.bgsegm.createBackgroundSubtractorMOG()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()