import PIL.Image
import scipy.misc
import numpy as np

"""
    ;Author chenhao
    ;Date 2018/12/7
"""

# 图像处理_对比增强
# 幂次变化 http://accu.cc/content/pil/contrast/
def conver_3d(img):
    s = np.empty(img.shape, dtype = np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            s[i][j] = (img[i][j]/255)**0.67*255
    return s

img = PIL.Image.open("./image/day02/source.jpg")
im_mat = scipy.misc.fromimage(img)
im_converted_mat = conver_3d(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.save("./image/day02/source_enhand.jpg")

# 图像处理_对比拉伸
# 公式 T(x) = (x - rmin)/(rmax - rmin) * 255
def convert_2d(r):
    rmin = np.min(r)
    rmax = np.max(r)
    if rmin == rmax:
        return r
    s = np.empty(r.shape, dtype=np.uint8)
    for j in range(r.shape[0]):
        for i in range(r.shape[1]):
            s[j][i] = (r[j][i] - rmin) / (rmax - rmin) * 255
    return s

def convert_3ds(r):
    s_dsplit = []
    for d in range(r.shape[2]):
        rr = r[:, :, d]
        ss = convert_2d(rr)
        s_dsplit.append(ss)
    s = np.dstack(s_dsplit)
    return s

im = PIL.Image.open("./image/day02/source.jpg")
im_mat = scipy.misc.fromimage(im)
im_converted_mat = convert_3ds(im_mat)
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.save("./image/day02/source_extend.jpg")

# 图像处理_位图切割
# 像素由 8 比特表示，将图像转化为1到8比特平面；4~7有重要数据
flat = 7 # 取第几位图像

def img_apart(img):
    s = np.empty(img.shape, dtype=np.uint8)
    for j in range(img.shape[0]):
        for i in range(img.shape[1]):
            bits = bin(img[j][i])[2:].rjust(8, '0')
            fill = int(bits[-flat - 1])
            s[j][i] = 255 if fill else 0
    return s

img = PIL.Image.open("./image/day02/source.jpg")
img = img.convert("L")
img_mat = scipy.misc.fromimage(img)
img_apart = img_apart(img_mat)
img = PIL.Image.fromarray(img_apart)
img.save("./image/day02/source_apart7.jpg")
