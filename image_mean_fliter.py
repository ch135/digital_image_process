import numpy as np
import PIL.Image
import scipy.misc
import scipy.signal
"""
    ;Author 陈浩
    ;Date 2018/12/9
    ;Detail 数字图像处理_空间处理_均值滤波
        均值滤波器的输出是包含在滤波掩模领域内像素的简单平均值。
"""
path = "./image/day04/"


def convert_2d(r):
    n = 3
    window = np.ones((n, n))/n**2
    s = scipy.signal.convolve2d(r, window, mode="same", boundary="symm")
    return s.astype(np.uint8)


def convert_3d(r):
    s_split = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        ss = convert_2d(rr)
        s_split.append(ss)
    s = np.dstack(s_split)
    return s


img = PIL.Image.open(path+"source.jpg")
img_mat = scipy.misc.fromimage(img)
img_convert_mat = convert_3d(img_mat)
img = PIL.Image.fromarray(img_convert_mat)
img.save(path+"source_mean_filter.jpg")
