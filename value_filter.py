import numpy as np
import PIL.Image
import scipy.misc
import scipy.ndimage
"""
    ;Author 陈浩
    ;Date 2018/12/9
    ;Detail 数字图像处理_空间处理_中值滤波
        利用图像滤波器包围的图像区域中像素的统计排序, 然后由统计排序结果的值代替中心像素的值；处理椒盐噪声（黑白点）很有效
"""
path = "./image/day04/"


def convert_2d(r):
    n = 10
    s = scipy.ndimage.median_filter(r, (n, n))
    return s.astype(np.uint8)


def convert_3d(r):
    s_dsplit = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        ss = convert_2d(rr)
        s_dsplit.append(ss)
    s = np.dstack(s_dsplit)
    return s


im = PIL.Image.open(path+"source_value_filter.jpg")
im_mat = scipy.misc.fromimage(im)
im_converted_mat = convert_3d(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.save(path+"source_value_filter.jpg")
