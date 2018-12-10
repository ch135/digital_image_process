import numpy as np
import scipy.misc
import PIL.Image
import matplotlib.pyplot as plt
"""
    ;Author 陈浩
    ;Date 2018/12/9
    ;Detail 数字图像处理_频率滤波
       傅里叶变换(Fourier transform)是一种线性的积分变换, 常在将信号在时域(或空域)和频域之间变换时使用。
       经过傅里叶变换而生成的函数 fˆ 称作原函数 f 的傅里叶变换、亦或其频谱. 在许多情况下, 傅里叶变换是可逆的, 
       即可通过 fˆ 得到其原函数 f .通常情况下, f 是实数函数, 而 fˆ 则是复数函数, 用一个复数来表示振幅和相位.
"""
path = "./image/day04/"

img = PIL.Image.open(path+"source.jpg")
img = img.convert("L")
img_mat = scipy.misc.fromimage(img)
rows, cols = img_mat.shape

# 扩展 M * N 图像到 2M * 2N
img_mat_ext = np.zeros((2*rows, 2*cols))
for i in range(rows):
    for j in range(cols):
        img_mat_ext[i][j] = img_mat[i][j]

# 快速傅里叶变换得到频率分布
img_mat_fu = np.fft.fft2(img_mat_ext)
# 将低频信号移植中间, 等效于在时域上对 f(x, y) 乘以 (-1)^(m + n)
img_mat_fu = np.fft.fftshift(img_mat_fu)

# 显示原图
plt.subplot(121)
plt.imshow(img_mat, "gray")
plt.title("original")
plt.subplot(122)
# 在显示频率谱之前, 对频率谱取实部并进行对数变换
plt.imshow(np.log(abs(img_mat_fu)), "gray")
plt.title("fourier")
plt.show()

# 傅里叶反变换
im_converted_mat = np.fft.ifft2(np.fft.ifftshift(img_mat_fu))
# 得到傅里叶反变换结果的实部
im_converted_mat = np.abs(im_converted_mat)
# 提取左上象限
im_converted_mat = im_converted_mat[0:rows, 0:cols]
# 显示图像
im_converted = PIL.Image.fromarray(im_converted_mat)
im_converted.save(path+"source_fourier.gif")
