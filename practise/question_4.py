# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:32
# @Author  : chenhao
# @FileName: question_4.py
# @Software: PyCharm
# @Desc: Otsu 的二进制转换。Otsu二值化也叫判别分析，是一种自动确定二值化分离阙值的方法
#        Sb ^ 2 = w0 * w1 *（M0-M1）^ 2
import cv2
import numpy as np

img = cv2.imread("practise.jpg").astype(np.float)

h, w, c = img.shape

out = 0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2]
out = out.astype(np.uint8)

max_sigma = 0
max_t = 0

for t in range(1, 255):
    v0 = out[np.where(out < t)]
    m0 = np.mean(v0) if len(v0) > 0 else 0.
    w0 = len(v0) / (h * w)
    v1 = out[np.where(out >= t)]
    m1 = np.mean(v1) if (len(v1) > 0) else 0.
    w1 = len(v1) / (h * w)
    sigma = w0 * w1 * (m1 - m0) ** 2
    if sigma > max_sigma:
        max_sigma = sigma
        max_t = t

threshold = max_t
print(threshold)
out[out < threshold] = 0
out[out >= threshold] = 255

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
