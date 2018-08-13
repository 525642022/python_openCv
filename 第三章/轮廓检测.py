# 作者 ljc
import cv2
import numpy as np

# 创建一个200x200大小的黑色空白图像
img = np.zeros((200, 200), dtype=np.uint8)
#黑色图像中放置一个100x100的白色方块
img[50:150, 50:150] = 255

ret, thresh = cv2.threshold(img, 127, 255, 0)
# 参数 1 输入图像 2层次类型 3 轮廓逼近方法
# 函数特性：
# 1.这个函数会修改输入图像，建议输入时使用原始图像拷贝 .copy
# 2.由函数返回的层次树相当重要
# (1)cv2.RETE_TREE 会得到图像中轮廓的整体层次结构，以此建立轮廓间的关系
# (2)cv2.RETE_EXTERNAL 只得到最外面的轮廓，这可以消除其他轮廓中的轮廓
# 返回值：修改后的图像，图像轮廓，图像的层次
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

img = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow('contours', color)
cv2.waitKey()
cv2.destroyAllWindows()
