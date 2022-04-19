"""
Author:XiaoMa
date:2021/11/2
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread("./da4.png")
img1 = img0
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
h, w = img1.shape[:2]
print(h, w)
cv2.namedWindow("W0")
cv2.imshow("W0", img2)
cv2.waitKey(delay=0)
# 图像进行二值化
##第一种阈值类型
ret0, img3 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
print(ret0)
##第二种阈值类型
ret1, img4 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY_INV)
print(ret1)
##第三种阈值类型
ret2, img5 = cv2.threshold(img2, 127, 255, cv2.THRESH_TRUNC)
print(ret2)
##第四种阈值类型
ret3, img6 = cv2.threshold(img2, 127, 255, cv2.THRESH_TOZERO)
print(ret3)
##第五种阈值类型
ret4, img7 = cv2.threshold(img2, 127, 255, cv2.THRESH_TOZERO)
print(ret4)
# 将所有阈值类型得到的图像绘制到同一张图中
plt.rcParams['font.family'] = 'SimHei'  # 将全局中文字体改为黑体
figure = [img2, img3, img4, img5, img6, img7]
title = ["原图", "第一种阈值类型", "第二种阈值类型", "第三种阈值类型", "第四种阈值类型", "第五种阈值类型"]
for i in range(6):
    figure[i] = cv2.cvtColor(figure[i], cv2.COLOR_BGR2RGB)  # 转化图像通道顺序，这一个步骤要记得
    plt.subplot(3, 2, i + 1)
    plt.imshow(figure[i])
    plt.title(title[i])  # 添加标题
plt.show()
