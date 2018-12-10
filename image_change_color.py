import numpy as np
import PIL.Image
import scipy.misc
"""
 ;Author chenhao
    ;Date 2018/12/10
    ;Detail 数字图像处理_补色与反色
"""
path = "./image/day05/"

# 补色
def add_color(r):
    img_convert_mat = np.zeros_like(r, np.uint8)
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            # 补色公式：max(r, g, b) + min(r, g, b) - [r g b]
            maxrgb = r[i][j].max()
            minrgb = r[i][j].min()
            img_convert_mat[i][j] = (int(maxrgb)+int(minrgb)*np.ones(3)-r[i][j])
    return img_convert_mat


# 反色
def anti_color(r):
    # 反色公式：[255, 255, 255] - [R, G, B]
    img_convert_mat = np.ones_like(r)*255 - img_mat
    return img_convert_mat


img = PIL.Image.open(path+"source.jpg")
img = img.convert("RGB")
img_mat = scipy.misc.fromimage(img)
img = anti_color(img_mat)
img_convert = PIL.Image.fromarray(img)
img_convert.save(path+"source_anti.jpg")
