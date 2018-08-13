# 作者 ljc
import cv2
import filters

img = cv2.imread('out.jpg')
filter = filters.BlurFilter()
filter.apply(img,img)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
