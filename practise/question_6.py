# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 19:21
# @Author  : chenhao
# @FileName: question_6.py
# @Software: PyCharm
# @Desc: 色彩还原处理
#     val = {32（0 < = val <   64）
#              96（64 < = val < 128）
#             160（128 < = val < 192）
#             224（192 < = val < 256）
import cv2
img = cv2.imread("practise.jpg")

out = img//64*64+32

cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
