# 作者 ljc
import cv2
import numpy

# 将颜色装换为灰度图
img = cv2.imread('mmm.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 设置阈值将图像分为两个部分 黑色部分与白色部分

ret, thresh = cv2.threshold(gray, 0, 255,
                            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# 通过morphologyEx变换来去除噪声数据，这是对图像进行膨胀后再进行腐蚀的操作
# 他可以提取图像特征可
kernl = numpy.ones((3, 3), numpy.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN,
                           kernl, iterations=2)
# 通过morphologyEx后 图像再进行膨胀操作可以得到大部分的背景区域
sure_bg = cv2.dilate(opening, kernl, iterations=3)

# 反之，可以通过distanceTransform来获取前景区域
# 也就是说越是远离背景区域的点，越是可能属于前景
# 在得到distanceTransform操作结果之后，应用一个阈值来决定那些区域的远景
# 这样的到正确结果的概率很高
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform,
                             0.7 * dist_transform.max(),
                             255, 0)
# 使用前景区域与后景区域的集合相减来得到重合部分
sure_fg = numpy.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# 现在有了这些区域我们就可以设定栅栏来阻止水的汇聚了，这是通过connectedComponents
# 函数来完成的。我们把图像看做是一个有边相连的节点集，给出一定的前景区域
# 其中一些节点会连接在一起，而另一些节点没有连接在一起。这就意味着，他们属于不同的山谷
# 在他们之间应该有一个栅栏
ret, markets = cv2.connectedComponents(sure_fg)
# 在背景上加一这会将unknow区域设为0

markets = markets + 1
markets[unknown == 255] = 0

# 最后打开大门，让水把栅栏绘制成红色

markets = cv2.watershed(img, markets)
img[markets == -1] = [255, 0, 0]
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()
