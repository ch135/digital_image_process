import numpy as np
import PIL.Image
import scipy.misc
"""
 ;Author chenhao
    ;Date 2018/12/10
    ;Detail 双三次插值（双立方插值） http://accu.cc/content/pil/resize_bicubic/
       函数 f 在点 (x,y) 的值可以通过矩形网格中最近的十六个采样点的加权平均得到, 
       在这里需要使用两个多项式插值三次函数, 每个方向使用一个.
"""
path = "./image/day05/"

def get_item(arr, *args):
    indexes = []
    for i, entry in enumerate(args):
        index = entry
        if index < 0:
            index = abs(index) - 1
        if index >= arr.shape[i]:
            index = arr.shape[i] - index % arr.shape[i] - 1
        indexes.append(index)
    r = arr
    for index in indexes:
        r = r[index]
    return r


def get_w(x):
    a = -0.5
    absx = abs(x)
    if absx <= 1:
        return (a + 2) * absx**3 - (a + 3) * absx ** 2 + 1
    elif 1 < absx < 2:
        return a * absx**3 - 5 * a * absx**2 + 8 * a * absx - 4 * a
    else:
        return 0


im = PIL.Image.open(path+"source.jpg")
im_mat = scipy.misc.fromimage(im)
im_mat_resized = np.empty((270, 480, im_mat.shape[2]), dtype=np.uint8)

for r in range(im_mat_resized.shape[0]):
    for c in range(im_mat_resized.shape[1]):
        # 目标图像与原图像像素点坐标对应
        rr = (r + 1) / im_mat_resized.shape[0] * im_mat.shape[0] - 1
        cc = (c + 1) / im_mat_resized.shape[1] * im_mat.shape[1] - 1

        rr_int = int(rr)
        cc_int = int(cc)

        sum_p = np.empty(im_mat.shape[2])
        # 求每个像素点的 Bicubic 值像素值
        for j in range(rr_int - 1, rr_int + 3):
            for i in range(cc_int - 1, cc_int + 3):
                w = get_w(rr - j) * get_w(cc - i)
                p = get_item(im_mat, j, i) * w
                sum_p += p

        for i, entry in enumerate(sum_p):
            sum_p[i] = min(max(entry, 0), 255)

        im_mat_resized[r][c] = sum_p

im_resized = PIL.Image.fromarray(im_mat_resized)
im_resized.save(path+"source_bicubic.jpg")