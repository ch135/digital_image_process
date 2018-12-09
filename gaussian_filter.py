import PIL.Image
import PIL.ImageFilter
"""
    ;Author 陈浩
    ;Date 2018/12/9
    ;Detail 数字图像处理_空间处理_高斯滤波
       高斯模糊后的灰度值与"周围像素"的噪声以及细节层次降低了, 亦即"模糊"了.
       正则化分布 = 高斯分布
"""
path = "./image/day04/"
im = PIL.Image.open(path+'source.jpg')
im = im.filter(PIL.ImageFilter.GaussianBlur(radius=2))
im.save(path+"source_gaussian.jpg")
