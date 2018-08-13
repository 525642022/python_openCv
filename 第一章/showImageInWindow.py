# 作者 ljc
# imshow函数有两个参数，显示图像的帧名称和要显示的图像本身
# destroyAllWindows函数 释放有openCv创建的所有窗口


import cv2
import  numpy as np

img = cv2.imread('out.jpg')
cv2.imshow('out',img)
cv2.waitKey()
cv2.destroyAllWindows()