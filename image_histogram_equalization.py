import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import scipy.misc

"""
    ;Author chenhao
    ;Date 2018/12/8 
"""
path = "./image/day03/"

# 图像处理_直方图均衡化（http://accu.cc/content/pil/histogram_equalization/）
def ratio_average(r):
    x = np.zeros([256])
    # 求么每个灰度值概率
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            x[r[i][j]]+=1
    x = x/r.size

    # 每个概率加上前面所有概率，替换当前概率
    sum_x = np.zeros([256])
    for i, _ in enumerate(x):
        sum_x[i] = sum(x[:i])

    # 每个概率*255，做为新图片灰度值
    s = np.empty(r.shape, dtype=np.uint8)
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            s[i][j] = 255 * sum_x[r[i][j]]
    return s
    
img = PIL.Image.open(path+"source.jpg")
img = img.convert("L")
img_mat = scipy.misc.fromimage(img)
source_img = PIL.Image.fromarray(img_mat)
source_img.save(path+"souece_l.jpg")
# 显示原始直方图
plt.hist(img_mat.reshape([img_mat.size]), 256, density=1)
plt.show()

# 显示均匀直方图
img_converted_mat = ratio_average(img_mat)
plt.hist(img_converted_mat.reshape([img_converted_mat.size]), 256, density=1)
plt.show()

img = PIL.Image.fromarray(img_converted_mat)
img.save(path+"source_averge.jpg")
