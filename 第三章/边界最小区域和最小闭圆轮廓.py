# 作者 ljc
# 实现边界框 最小矩形区域面积 最小闭合圆
import cv2
import numpy

img = cv2.pyrDown(cv2.imread('test.jpeg', cv2.IMREAD_UNCHANGED))
src = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)
image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # 计算边界框
    x, y, w, h = cv2.boundingRect(c)
    # 画出这个边界框的矩形
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 寻找最小区域
    rect = cv2.minAreaRect(c)
    # 计算最小矩形框的面积
    box = cv2.boxPoints(rect)
    # 将面积转换为int
    box = numpy.int0(box)
    # 画出区域
    # 参数 源图片，矩形管区域，颜色 ，迷得
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    # 计算最小闭合区域的半径和中心 检测最小闭合圆
    # minEnclosingCircle 返回值为中心点元组与最小半径
    (x, y), radius = cv2.minEnclosingCircle(c)
    # 转换int
    center = (int(x), int(y))
    radius = int(radius)
    # 画圆
    img = cv2.circle(img, center, radius, (0, 255, 0), 2)
cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow('contour', img)
cv2.waitKey()
cv2.destroyAllWindows()
