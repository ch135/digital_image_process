import PIL.Image
import PIL.ImageFilter
import scipy.misc
import numpy as np
"""
    ;Author: chenhao
    ;Date: 2018/12/8
    ;Detail: 取得原图与其高斯模糊图像的差值图像
"""
path = "./image/day03/"

def convert_2d(r, h):
    # 矩阵减法：减去最小像素
    s = r - h
    if np.min(s) >= 0 and np.max(s) <= 255:
        return s
    # 线性拉伸：使像素值保持在0~255
    s = s - np.full(s.shape, np.min(s))
    s = s * 255 / np.max(s)
    s = s.astype(np.uint8)
    return s

def convert_3d(r, h):
    s_dsplit = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        hh = h[:, :, d]
        ss = convert_2d(rr, hh)
        s_dsplit.append(ss)
    s = np.dstack(s_dsplit)
    return s


im = PIL.Image.open(path+"source.jpg")
im = im.convert('RGB')
im_mat = scipy.misc.fromimage(im)
# 高斯模糊
im_converted = im.filter(PIL.ImageFilter.GaussianBlur(radius=2))
im_converted_mat = scipy.misc.fromimage(im_converted)
im_sub_mat = convert_3d(im_mat, im_converted_mat)
im_sub = PIL.Image.fromarray(im_sub_mat)
im_sub.save(path+"source_sub.jpg")
