import cv2
from rgb2yuv import rgb2yuv
from rgb2yuv420 import RGB2YUV420 as yuv420
from dct import DCT
from quantization import quantization,QF2Qtable_y,QF2Qtable_c

def compression(image,QF):
    #输入图片,QF 输出量化DCT系数组成的列表
    image_y, image_u, image_v = yuv420(image)
    image_dct_y = DCT(image_y)
    image_dct_u = DCT(image_u)
    image_dct_v = DCT(image_v)
    Q_y = QF2Qtable_y(QF)
    Q_c = QF2Qtable_c(QF)
    img_y_quan = quantization(image_dct_y, Q_y)
    img_u_quan = quantization(image_dct_u, Q_c)
    img_v_quan = quantization(image_dct_v, Q_c)

QF = 71
image = cv2.imread('../DL_data/4.ppm')
#cv2.imshow('1',image)
#cv2.waitKey(0)
#输入512*512 彩色rgb图像；共(512/16)*(512/16)*4=4096个Y块，1024个C_b块和1024个C_r块
image_y, image_u, image_v = yuv420(image)
image_dct_y = DCT(image_y)
#image_dct_u = DCT(image_u)
#image_dct_v = DCT(image_v)
Q_y = QF2Qtable_y(QF)
#Q_c = QF2Qtable_c(QF)
img_y_quan = quantization(image_dct_y, Q_y)
#img_u_quan = quantization(image_dct_u, Q_c)
#img_v_quan = quantization(image_dct_v, Q_c)
