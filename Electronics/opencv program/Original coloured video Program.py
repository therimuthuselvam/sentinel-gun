# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:34:16 2019

@author: Ragavan Rana
"""

import cv2
cap = cv2.VideoCapture(0)

while True:
    if cap.grab():
        flag, frame = cap.retrieve()
        if not flag:
            continue
        else:
            cv2.imshow('video', frame)
    if cv2.waitKey(10) == 27:
        break