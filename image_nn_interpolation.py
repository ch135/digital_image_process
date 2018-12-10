import PIL.Image
"""
 ;Author chenhao
    ;Date 2018/12/10
    ;Detail 数字图像处理_最近邻插值（http://accu.cc/content/pil/resize_nearst/）
        近邻取样插值法是将目标图像各点的像素值设为原图像中与其最近的点
"""
path = "./image/day05/"
im = PIL.Image.open(path+"source.jpg")
im_resized = PIL.Image.new(im.mode, (480, 270))
for r in range(im_resized.size[1]):
    for c in range(im_resized.size[0]):
        rr = round((r+1) / im_resized.size[1] * im.size[1]) - 1
        cc = round((c+1) / im_resized.size[0] * im.size[0]) - 1
        # putpixel() 设置某个点的像素值
        im_resized.putpixel((c, r), im.getpixel((cc, rr)))
im_resized.save(path+"source_nn_interpolation.jpg")

