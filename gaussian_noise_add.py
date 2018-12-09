import PIL.Image
import scipy.misc
import numpy as np
"""
    ;Author chenhao
    ;Date 2018/12/9
    ;Detail 加性高斯白噪音
"""
# 加噪
path = "./image/day04/"


def convert_2d(r):
    s = r+np.random.normal(0, 64, r.shape)
    if np.min(s)>=0 and np.max(s)<=255:
        return s

    s = s-np.full(s.shape, np.min(s))
    s = s*255/np.max(s)
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


img = PIL.Image.open(path+"source.jpg")
img = img.convert("RGB")
img_mat = scipy.misc.fromimage(img)
img_convert = convert_3d(img_mat)
img = PIL.Image.fromarray(img_convert)
img.save(path+"source_add_noise.jpg")
