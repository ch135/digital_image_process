import numpy as np
import PIL.Image
import scipy.misc
"""
    ;Author chenhao
    ;Date 2018/12/10
    ;Detail 频率滤波_低通滤波
        去除图像的边缘或尖锐的高频信息，保留中间的低频信息
"""
path = "./image/day05/"


# 理想低通滤波
def convert_2d(r):
    r_ext = np.zeros((r.shape[0] * 2, r.shape[1] * 2))
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            r_ext[i][j] = r[i][j]

    r_ext_fu = np.fft.fft2(r_ext)
    r_ext_fu = np.fft.fftshift(r_ext_fu)
    # 截至低频为 100
    d = 100
    center = (r_ext_fu.shape[0]//2, r_ext_fu.shape[1]//2)
    h = np.empty(r_ext_fu.shape)
    for i in range(r_ext_fu.shape[0]):
        for j in range(r_ext_fu.shape[1]):
            duv = ((i-center[0])**2 + (j-center[1])**2)**0.5
            h[i, j] = duv < d

    r_ext_fu = r_ext_fu * h
    r_ext_fu = np.fft.ifft2(np.fft.fftshift(r_ext_fu))
    r_ext_fu = np.abs(r_ext_fu)
    s = r_ext_fu[0:r.shape[0], 0:r.shape[1]]

    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = min(max(0, s[i][j]), 255)
    return s.astype(np.uint8)


# 巴特沃斯低通滤波器（BLPF）
# BLPF将低频与高频之间平滑过渡，没有产生可见振铃效果
def convert_blpf_2d(r):
    r_ext = np.zeros((r.shape[0] * 2, r.shape[1] * 2))
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            r_ext[i][j] = r[i][j]

    r_ext_fu = np.fft.fft2(r_ext)
    r_ext_fu = np.fft.fftshift(r_ext_fu)
    # 截至低频为 100
    d = 100
    # 2 阶巴特沃斯
    n = 2
    center = (r_ext_fu.shape[0]//2, r_ext_fu.shape[1]//2)
    h = np.empty(r_ext_fu.shape)
    for i in range(r_ext_fu.shape[0]):
        for j in range(r_ext_fu.shape[1]):
            duv = ((i-center[0])**2 + (j-center[1])**2)**0.5
            h[i, j] = 1/(1+(duv/d))**(2*n)

    r_ext_fu = r_ext_fu * h
    r_ext_fu = np.fft.ifft2(np.fft.fftshift(r_ext_fu))
    r_ext_fu = np.abs(r_ext_fu)
    s = r_ext_fu[0:r.shape[0], 0:r.shape[1]]

    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = min(max(0, s[i][j]), 255)
    return s.astype(np.uint8)


# 高斯低通滤波
def convert_gaussian_2d(r):
    r_ext = np.zeros((r.shape[0] * 2, r.shape[1] * 2))
    for i in range(r.shape[0]):
        for j in range(r.shape[1]):
            r_ext[i][j] = r[i][j]

    r_ext_fu = np.fft.fft2(r_ext)
    r_ext_fu = np.fft.fftshift(r_ext_fu)

    # 截止频率为 100
    d0 = 100
    # 频率域中心坐标
    center = (r_ext_fu.shape[0] // 2, r_ext_fu.shape[1] // 2)
    h = np.empty(r_ext_fu.shape)
    # 绘制滤波器 H(u, v)
    for u in range(h.shape[0]):
        for v in range(h.shape[1]):
            duv = ((u - center[0]) ** 2 + (v - center[1]) ** 2) ** 0.5
            h[u][v] = np.e ** (-duv**2 / d0 ** 2)

    s_ext_fu = r_ext_fu * h
    s_ext = np.fft.ifft2(np.fft.ifftshift(s_ext_fu))
    s_ext = np.abs(s_ext)
    s = s_ext[0:r.shape[0], 0:r.shape[1]]

    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            s[i][j] = min(max(s[i][j], 0), 255)

    return s.astype(np.uint8)


def convert_3d(r):
    s_spilt = []
    for i in range(r.shape[2]):
        rr = r[:, :, i]
        s_convert = convert_gaussian_2d(rr)
        s_spilt.append(s_convert)
    s = np.dstack(s_spilt)
    return s


img = PIL.Image.open(path+"source.jpg")
img_mat = scipy.misc.fromimage(img)
img_convert_mat = convert_3d(img_mat)
img = PIL.Image.fromarray(img_convert_mat)
img.save(path+"source_filter_low_gaussian.jpg")




