# 作者 ljc
import cv2
import numpy
# imread () 函数会删除所有的alpha通道信息（透明度）
# imwrite（）要求图像格式为BGR或灰度图，并且每个通道要有一定的位（bit）
# 输出格式要支持这些通道
grayImage = cv2.imread("test.png",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("test1.png",grayImage)
