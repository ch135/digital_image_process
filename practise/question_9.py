# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 20:13
# @Author  : chenhao
# @FileName: question_9.py
# @Software: PyCharm
# @Desc: 高斯滤波
import cv2
import numpy as np

img = cv2.imread("practise.jpg")

H, W, C = img.shape

K_size = 3
sigma = 1.3

pad = K_size // 2
out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=np.float)
out[pad:pad + H, pad:pad + W] = img.copy().astype(np.float)

K = np.zeros((K_size, K_size), dtype=np.float)
for x in range(-pad, -pad + K_size):

    for y in range(-pad, -pad + K_size):
        K[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
K /= (sigma * np.sqrt(2 * np.pi))
K /= K.sum()

tmp = out.copy()

for x in range(H):
    for y in range(W):
        for c in range(C):
            out[pad+x, pad+y, c] = np.sum(K * tmp[x:x+K_size, y:y + K_size, c])
out = out[pad:pad + H, pad:pad + W].astype(np.uint8)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
