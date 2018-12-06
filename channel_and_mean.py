import scipy.misc
import PIL.Image
import PIL.ImageStat

"""
    ;Author: chenhao
    ;Date: 2018/12/6
"""
img = scipy.misc.imread("./image/source.jpg")
print(img.shape)    # 960*960*3

# 取 R G B 层图像
img1=PIL.Image.open("./image/source.jpg")
r, g, b = img1.split()

r.save("./image/source_r.jpg")
g.save("./image/source_g.jpg")
b.save("./image/source_b.jpg")

# 交换通道
img2 = PIL.Image.open("./image/source.jpg")
r, g, b = img2.split()
im = PIL.Image.merge("RGB", (r, b, g))
im.save("./image/source_chage.jpg")

# 自定义通道
img3 = PIL.Image.open("./image/source.jpg")
_, g, b = img3.split()
r = PIL.Image.new("L", im.size, color=100)
im = PIL.Image.merge("RGB", (r, g, b))
im.save("./image/source_diy.jpg")


# 图像均值（特征标准化、均值滤波、主题色提取）
img4 = PIL.Image.open("./image/source.jpg")
mean = PIL.ImageStat.Stat(img4).mean
print(mean)

# 改变色彩模式；模式包含 RGB、1、L、P、RGBA、CMYK、YCbCr、F
img5 = PIL.Image.open("./image/source.jpg")
rgb2xyz= (
 
             0.412453,0.357580, 0.180423, 0,
 
                       0.212671,0.715160, 0.072169, 0,
 
                       0.019334,0.119193, 0.950227, 0 )
im = img5.convert("RGB", rgb2xyz)   
im.save("./image/image_rgb.gif")
