# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 19:10
# @Author  : chenhao
# @FileName: question_5.py
# @Software: PyCharm
# @Desc: HSV转换
import cv2
import numpy as np

img = cv2.imread("practise.jpg").astype(np.float32) / 255.

out = np.zeros_like(img)

max_v = np.max(img, axis=2).copy()
min_v = np.min(img, axis=2).copy()
min_arg = np.argmin(img, axis=2)

H = np.zeros_like(max_v)

H[np.where(max_v == min_v)] = 0
## if min == B
ind = np.where(min_arg == 0)
H[ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60
## if min == R
ind = np.where(min_arg == 2)
H[ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180
## if min == G
ind = np.where(min_arg == 1)
H[ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300

V = max_v.copy()
S = max_v.copy() - min_v.copy()

# Transpose Hue
H = (H + 180) % 360

# HSV > RGB

C = S
H_ = H / 60
X = C * (1 - np.abs(H_ % 2 - 1))
Z = np.zeros_like(H)

vals = [[Z, X, C], [Z, C, X], [X, C, Z], [C, X, Z], [C, Z, X], [X, Z, C]]

for i in range(6):
    ind = np.where((i <= H_) & (H_ < (i + 1)))
    out[..., 0][ind] = (V - C)[ind] + vals[i][0][ind]
    out[..., 1][ind] = (V - C)[ind] + vals[i][1][ind]
    out[..., 2][ind] = (V - C)[ind] + vals[i][2][ind]

out[np.where(max_v == min_v)] = 0
out = (out * 255).astype(np.uint8)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

