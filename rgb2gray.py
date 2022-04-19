import cv2
import numpy as np

xmin, ymin, w, h = 470, 1020, 995, 30
image  = cv2.imread('./da0.png')#要找的大图
imgCrop = image[ymin:ymin+h, xmin:xmin+w]
ret1, imgCrop = cv2.threshold(imgCrop, 127, 255, cv2.THRESH_BINARY_INV)
imgCrop = cv2.cvtColor(imgCrop , cv2.COLOR_BGR2RGB)
cv2.imshow('girl_gray', imgCrop)
cv2.imwrite("da00.png",imgCrop)
cv2.waitKey(delay = 0)
