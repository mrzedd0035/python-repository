# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:56:34 2021

@author: mrzed
"""

import cv2
frame = "tree.jfif"
img_gray = cv2.imread(fname, 0)
img_color = cv2.imread(fname, 1)

h_new = img_gray.shape[0]//2
w_new = img_color.shape[1]//2
img_gnew = cv2.resize(img_gray, (w_new, h_new))
img_cnew = cv2.resize(img_color, (w_new, h_new))

cv2.imshow('gray', img_gnew)
cv2.imshow('color', img_cnew)

fname_new = "tree_resized.jfif"
cv2.imwrite(fname_new, img_cnew)
cv2.waitKey(0)
cv2.destroyAllWindows