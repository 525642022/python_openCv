# 作者 ljc
# 将某一个目标点改变颜色
import cv2 as cv
import numpy as np

img = cv.imread('out.jpg')

#打印当前点的颜色
print(img.item(100, 10, 2))

img.itemset((100, 10, 2), 127)

#打印当前点的颜色
print(img.item(100, 10, 2))

cv.imwrite('111.jpg', img)