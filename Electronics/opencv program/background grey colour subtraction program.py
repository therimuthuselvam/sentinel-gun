# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 23:10:59 2019

@author: Theriselvam
"""

import numpy as np
import cv2

video = "xx.avi"
cap = cv2.VideoCapture(0)
bg = cv2.imread('rough.jpg',0)
#bg = cv2.imread("background.jpg")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    original_frame = frame.copy()
    if ret:
        # get foremask?
        fgmask = gray - bg

        # filter kernel for denoising:
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

        opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        # Dilate to merge adjacent blobs
        dilation = cv2.dilate(closing, kernel, iterations = 2)

        # show fg:dilation
        cv2.imshow('fg mask', dilation)
        cv2.imshow('original', original_frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
    else:
        break
