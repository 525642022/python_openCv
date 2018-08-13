# 作者 ljc
# 通过HoughLines和HoughLinesP来实现
# 差别：第一个函数使用标准的Hough来变换，第二个函数使用概率的Hough来变换
# HoughLinesP是通过分析点的子集并估计这些点都属于一条线的概率这是标准Hough的优化版
# 该函数的计算效率会高一些，执行会更快
# 参数 （1）需要吃力的图像
# （2）线段的几何表示rho和theta，一般分别取1 和np.pi/180
# （3）阈值 低于阈值的直线会被忽略
# （4）线的最小长度和最大....

import cv2
import numpy as np

img = cv2.imread('test.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 120)
minLineLength = 20
maxLinesGap = 5
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLinesGap)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('edges', edges)
cv2.imshow('lines', img)
cv2.waitKey()
cv2.destroyAllWindows()
