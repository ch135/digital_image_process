# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 20:08
# @Author  : chenhao
# @FileName: question_8.py
# @Software: PyCharm
# @Desc: 最大池化（Max Pooling）

import cv2
import numpy as np

img = cv2.imread("practise.jpg")

# Max Pooling
out = img.copy()

H, W, C = img.shape
G = 8
Nh = int(H / G)
Nw = int(W / G)

for y in range(Nh):
    for x in range(Nw):
        for c in range(C):
            out[G*y:G*(y+1), G*x:G*(x+1), c] = np.max(out[G*y:G*(y+1), G*x:G*(x+1), c])

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
