
import cv2
import numpy as np

# opencv 读取的图片是BGR顺序
# 色彩空间转换 BGR -> YUV

def rgb2yuv(image):
    h, w, c = image.shape
    image_yuv = np.zeros_like(image, dtype=np.uint8)
    for line in range(h):
        for row in range(w):
            B = image[line, row, 0]
            G = image[line, row, 1]
            R = image[line, row, 2]
            Y = np.round(0.299*R + 0.587*G + 0.114*B)
            U = np.round(0.5*R - 0.4187*G - 0.0813*G + 128)
            V = np.round(-0.1687*R - 0.3313*G + 0.5*B + 128)
            image_yuv[line, row, :] = (Y, U, V)
    return image_yuv

# 保存图像
#cv2.imwrite('Y.png', image_yuv[:,:, 0])
#cv2.imwrite('U.png', image_yuv[:,:, 1])
#cv2.imwrite('V.png', image_yuv[:,:, 2])     
#cv2.imwrite('YUV.png', image_yuv) 

