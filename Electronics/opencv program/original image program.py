# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:24:58 2019

@author: Theriselvam
"""
import cv2 as cv
imgFile = cv.imread('theri.jpg')

cv.imshow('theri', imgFile)
cv.waitKey(0)
cv.destroyAllWindows()