import numpy as np
import PIL.Image
import scipy.misc
import scipy.signal
"""
    ;Author 陈浩
    ;Date 2018/12/9
    ;Detail 数字图像处理_空间处理_锐化滤波
        使用拉普拉斯算子计算；应用强调图像中灰度的突变和降低灰度慢变化的区域. 这将产生一幅把图像中的浅灰色边线和突变点叠加到暗背景中的图像
"""
path = "./image/day04/"


def convert_2d(r):
    # 滤波掩模
    window = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    # 像素值如果大于 255 则取 255, 小于 0 则取 0
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = min(max(0, s[i][j]), 255)
    s = s.astype(np.uint8)
    return s


def convert_3d(r):
    s_dsplit = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        ss = convert_2d(rr)
        s_dsplit.append(ss)
    s = np.dstack(s_dsplit)
    return s


im = PIL.Image.open(path+"source.jpg")
im_mat = scipy.misc.fromimage(im)
im_converted_mat = convert_3d(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.save(path+"source_sharp.jpg")