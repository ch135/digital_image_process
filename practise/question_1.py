# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 15:50
# @Author  : chenhao
# @FileName: question_1.py
# @Software: PyCharm
# @Desc: 频道转换 rgb>>bgr
import cv2

img = cv2.imread("practise.jpg")
r = img[:, :, 0].copy()
g = img[:, :, 1].copy()
b = img[:, :, 2].copy()

img[:, :, 0] = b
img[:, :, 1] = g
img[:, :, 2] = r
cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
