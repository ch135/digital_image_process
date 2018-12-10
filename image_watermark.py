import PIL.Image
import scipy.misc
import numpy as np
"""
    ;Author chenhao
    ;Date 2018/12/10
    ;Detail 频率滤波_简单可见水印
        添加生成公式：fw=(1−α)f+αW
            α: 控制水印和衬底的相对可见性
            f: 衬底
            w: 水印图片
            注：当 w 为 RGBA 模式时, 参与计算的 α 需要乘以水印的 A 通道与 255 的比值.
        
        隐藏水印公式：fw=4(f/4)+w/64
            4*(f/4): 滤掉衬底最后2个低阶比特位
            w/64: 将 im_water 两个最高比特位移到衬底最低比特位
"""
path = "./image/day05/"


# 添加水印
def water_add(im, im_water):
    for i in range(im_water.shape[0]):
        for j in range(im_water.shape[1]):
            # im_water[i][j][-1]：取 A 通道的值
            a = 0.3 * im_water[i][j][-1] / 255
            im[i][j][0:3] = (1 - a) * im[i][j][0:3] + a * im_water[i][j][0:3]
    return im


# 隐藏水印
def water_hidden(im, im_water):
    im = im // 4 * 4
    for x in range(im_water.shape[0]):
        for y in range(im_water.shape[1]):
            im[x][y] += im_water[x][y]//64
    return im


im = scipy.misc.imread(path+"source.jpg", mode="RGBA")
im_water = scipy.misc.imread(path+"water.jpg", mode="RGBA")
im = water_hidden(im, im_water)
PIL.Image.fromarray(im.astype(np.uint8)).save(path+"source_water_hidden.gif")
# 提取水印
im = im % 4/3*255
PIL.Image.fromarray(im.astype(np.uint8)).save(path+"source_water_extract.gif")