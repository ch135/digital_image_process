# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:22
# @Author  : chenhao
# @FileName: question_3.py
# @Software: PyCharm
# @Desc: 二值化：将图像表示为黑白
import cv2
import numpy as np
img = cv2.imread("practise.jpg").astype(np.float)

r = img[:, :, 0].copy()
g = img[:, :, 1].copy()
b = img[:, :, 2].copy()

out = out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

threshold = 128
out[out < threshold] = 0
out[out >= threshold] = 255

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
