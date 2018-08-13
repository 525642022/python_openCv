# 作者 ljc
# 一个图像可以使用一个二维数组或一个三维和数组去表示
# 8位字节的灰度如就像一个二维数组，如Image[0,0]是255
# 24位的BGR图像则像一个三维数组，如image[0,0,0]是255，第一表示像素的y坐标，第二个表示像素的x坐标，第三值表示颜色通道
import cv2
import numpy
import os
# Make an array of 120,000 random bytes
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

#转换为400*300的灰度图
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('randomGray.png',grayImage)

#转换为400*100的GBR图
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('randomColor.png',bgrImage)