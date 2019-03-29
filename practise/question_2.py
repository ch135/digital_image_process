# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:12
# @Author  : chenhao
# @FileName: question_2.py
# @Software: PyCharm
# @Desc: 灰度 Y = 0.2126 R + 0.7152 G + 0.0722 B.
import cv2
import numpy as np
img = cv2.imread("practise.jpg").astype(np.float)
r = img[:, :, 0].copy()
g = img[:, :, 1].copy()
b = img[:, :, 2].copy()

# Gray scale
out = 0.2126 * r + 0.7152 * g + 0.0722 * b
out = out.astype(np.uint8)

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()

