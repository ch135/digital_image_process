# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 19:33
# @Author  : chenhao
# @FileName: question_7.py
# @Software: PyCharm
# @Desc: 平均合并(Average Pooling)
import cv2
import numpy as np

img = cv2.imread("practise.jpg")

out = img.copy()

H, W, C = out.shape
G = 8
NH = int(H / G)
NW = int(W / G)

for x in range(NH):
    for y in range(NW):
        for c in range(C):
            out[x * G:(x + 1) * G, y * G:(y + 1) * G, c] = np.mean(out[x * G:(x + 1) * G, y * G:(y + 1) * G, c]).astype(
                np.int)


cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
