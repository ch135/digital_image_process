import numpy as np
import matplotlib.pyplot as plt
"""
    ;Author chenhao
    ;Date 2018/12/10
    ;Detail 数字图像处理_噪声
        噪声概率密度函数
        高斯噪声；瑞利噪声；伽马（爱尔兰）噪声；指数噪声；均匀噪声；脉冲噪声（椒盐噪声）
"""
# 高斯噪声
x1 = np.random.normal(0, 64, (256, 256))
# 瑞丽噪声: (2/b)**0.5 为 1
x2 = np.random.rayleigh(scale=64, size=(256, 256))
# 伽马噪声：(b-1)/a 为2，放大 32 倍
x3 = np.random.gamma(shape=2, scale=32, size=(256, 256))
# 指数噪声：a = 1/32
x4 = np.random.exponential(scale=32, size=(256, 256))
# 均匀噪声
x5 = np.random.uniform(0, 1.0, (256, 256))
# 脉冲噪声
x6 = np.random.random_integers(0.1, 2.0, (256, 256))

for i, x in enumerate([x1, x2, x3, x4, x5, x6]):
    ax = plt.subplot(230+i+1)
    ax.hist(x.reshape(x.size), 64, normed=True)
    ax.set_yticks([])
    ax.set_xticks([])
plt.show()
