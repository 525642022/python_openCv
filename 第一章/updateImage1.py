# 作者 ljc
# 将图像的绿色值变为0
import cv2 as cv
import numpy as np

img = cv.imread('out.jpg')
print(img.shape)
print(img.size)
print(img.dtype)
# shape 包含 宽度，高度 和通道数
# size 图像像素的大小
# Datatype 图像的数据类型  如uint8
# cv.imwrite('111.jpg', img)