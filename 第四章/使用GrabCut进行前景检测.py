# 作者 ljc
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('out.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (0, 80, 1023, 1000)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5,
            cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
cv2.imshow('grabCut', img)
image = cv2.imread('out.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', image)
cv2.waitKey()
cv2.destroyAllWindows()
# plt.subplot(121)

# plt.show(img)
# plt.title('grabCut')
# plt.xticks([])
# plt.yticks([])
#
#
# plt.subplot(122)
# plt.show(image)
# plt.title("original")
# plt.xticks([])
# plt.yticks([])
# plt.show()
