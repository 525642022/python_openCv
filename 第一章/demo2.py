# 作者 ljc
import cv2
# 将图片由jpg转换为png
image = cv2.imread('out.jpg')
cv2.imwrite('test.png',image)