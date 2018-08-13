# 作者 ljc
import cv2
import numpy


class VConvolution(object):
    def __init__(self, kernel):
        self.__kernel = kernel

    def apply(self, src, dst):
        cv2.filter2D(src, -1, self.__kernel, dst)


# 锐化滤波器
class SharpenFilter(VConvolution):
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 9, -1],
                              [-1, -1, -1]])
        VConvolution.__init__(self, kernel)

#边缘检测滤波器
class FindEdgesFilter(VConvolution):
    def __init__(self):
        kernel = numpy.array([[-1, -1, -1],
                              [-1, 8, -1],
                              [-1, -1, -1]])
        VConvolution.__init__(self, kernel)


#模糊滤波器
class BlurFilter(VConvolution):
    def __init__(self):
        kernel = numpy.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04],
                              [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolution.__init__(self, kernel)