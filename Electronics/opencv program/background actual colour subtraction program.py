# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 00:05:18 2019

@author: Theriselvam
"""

import numpy as np
import cv2
video = "xx.avi"
cap = cv2.VideoCapture(0)
bg = cv2.imread("background.jpg")

while True:
    ret, frame = cap.read()
    original_frame = frame.copy()
    if ret:
        # get foremask?
        fgmask = frame - bg

        # filter kernel for denoising:
        gray_image = cv2.cvtColor(fgmask, cv2.COLOR_BGR2GRAY)
        thresh = 20
        im_bw = cv2.threshold(gray_image, thresh, 255, cv2.THRESH_BINARY)[1]
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