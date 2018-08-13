# 作者 ljc
# 从头开始学习openCv课程 这是第一天写的
import cv2
import numpy

# 创建一个黑色的正方图

img = cv2.imread('mmm.jpg')

# 将图片转换为BGR格式
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('mmm',img)
cv2.imwrite('mm.jpg',img)
cv2.waitKey()
cv2.destroyAllWindows()
