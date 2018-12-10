import numpy as np
import PIL.Image
import scipy.misc
"""
    ;Author chenhao
    ;Date 2018/12/10
    ;Detail 双线性插值
        取原图像中距离目标像素点最近的 4 个点, 并对这 4 个点与其对应权值的乘积求和, 获得最终像素值.
"""
path = "./image/day05/"
im = PIL.Image.open(path+"source.jpg")
im_mat = scipy.misc.fromimage(im)
im_mat_resized = np.empty((270, 480, im_mat.shape[2]), dtype=np.uint8)

for r in range(im_mat_resized.shape[0]):
    for c in range(im_mat_resized.shape[1]):
        rr = (r + 1) / im_mat_resized.shape[0] * im_mat.shape[0] - 1
        cc = (c + 1) / im_mat_resized.shape[1] * im_mat.shape[1] - 1

        rr_int = int(rr)
        cc_int = int(cc)

        if rr == rr_int and cc == cc_int:
            p = im_mat[rr_int][cc_int]
        elif rr == rr_int:
            p = im_mat[rr_int][cc_int] * (cc_int + 1 - cc) + im_mat[rr_int][cc_int + 1] * (cc - cc_int)
        elif cc == cc_int:
            p = im_mat[rr_int][cc_int] * (rr_int + 1 - rr) + im_mat[rr_int + 1][cc_int] * (rr - rr_int)
        else:
            p11 = (rr_int, cc_int)
            p12 = (rr_int, cc_int + 1)
            p21 = (rr_int + 1, cc_int)
            p22 = (rr_int + 1, cc_int + 1)

            dr1 = rr - rr_int
            dr2 = rr_int + 1 - rr
            dc1 = cc - cc_int
            dc2 = cc_int + 1 - cc

            w11 = dr2 * dc2
            w12 = dr2 * dc1
            w21 = dr1 * dc2
            w22 = dr1 * dc1

            p = im_mat[p11[0]][p11[1]] * w11 + im_mat[p21[0]][p21[1]] * w12 + \
                im_mat[p12[0]][p12[1]] * w21 + im_mat[p22[0]][p22[1]] * w22

        im_mat_resized[r][c] = p


im_resized = PIL.Image.fromarray(im_mat_resized)
im_resized.save(path+"source_bilinear.jpg")
