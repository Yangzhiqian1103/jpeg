import cv2
from rgb2yuv import rgb2yuv
from rgb2yuv420 import RGB2YUV420 as yuv420
from dct import DCT
from quantization import quantization,QF2Qtable_y,QF2Qtable_c
from label import label


Dataset_size = 1
image = cv2.imread('./4.ppm')

image_y, image_u, image_v = yuv420(image)
image_dct_y = DCT(image_y)
Q_y = QF2Qtable_y(QF = 71)
img_y_quan = quantization(image_dct_y, Q_y)
label_y = label(img_y_quan)
print(label_y)





