import cv2
import numpy as np

image  = cv2.imread('./da.png')#要找的大图
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow('girl_gray', image)
cv2.waitKey(0)
cv2.im