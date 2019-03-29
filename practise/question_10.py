# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 21:09
# @Author  : chenhao
# @FileName: question_10.py
# @Software: PyCharm
# @Desc: 中值滤波（中位数滤波）
import cv2
import numpy as np
img = cv2.imread("practise.jpg")
H, W, C = img.shape

K_size = 3

pad = K_size // 2
out = np.zeros((H + pad*2, W + pad*2, C), dtype=np.float)
out[pad:pad+H, pad:pad+W] = img.copy().astype(np.float)

tmp = out.copy()

for y in range(H):
    for x in range(W):
        for c in range(C):
            out[pad+y, pad+x, c] = np.median(tmp[y:y+K_size, x:x+K_size, c])

out = out[pad:pad+H, pad:pad+W].astype(np.uint8)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
