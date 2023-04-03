import math
import numpy as np

def alpha(u):
    if u==0:
        return 1/np.sqrt(8)
    else:
        return 1/2
 
def block_fill(block):
    block_size = 8
    dst = np.zeros((block_size, block_size), dtype=np.uint8)
    h, w = block.shape
    dst[:h, :w] = block   
    return dst
 
def DCT_block(img):
    #输入8*8 pixel block ，输出 DCT block
    block_size = 8
    img = block_fill(img)
    img_fp32 = img.astype(np.float32)
    img_dct = np.zeros((block_size, block_size), dtype=np.float32)
    for line in range(block_size):
        for row in range(block_size):
            n = 0
            for x in range(block_size):
                for y in range(block_size):
                    n += img_fp32[x,y]*math.cos(line*np.pi*(2*x+1)/16)*math.cos(row*np.pi*(2*y+1)/16)
            img_dct[line, row] = alpha(line)*alpha(row)*n
    return np.ceil(img_dct)
    
def DCT(image):
    #输入图片，输出由 DCT blocks 组成的 list
    block_size = 8
    h, w= image.shape
    dlist = []
    for i in range((h + block_size - 1) // block_size):
        for j in range((w + block_size - 1) // block_size):
            img_block = image[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
            # 处理一个像素块
            img_dct = DCT_block(img_block)
            dlist.append(img_dct)
    return dlist
 
# img_dct = DCT(image_y)
def IDCT_block(dct):
    #输入dct block 输出 pixel block
    #我不太确定我的这个逆变换写的对不对。。。
    block_size = 8
    dct = block_fill(dct)
    dct_fp32 = dct.astype(np.float32)
    img_pixel = np.zeros((block_size, block_size), dtype=np.float32)
    for line in range(block_size):
        for row in range(block_size):
            n = 0
            for x in range(block_size):
                for y in range(block_size):
                    n += alpha(x)*alpha(y)*dct_fp32[x,y]*math.cos(line*np.pi*(2*x+1)/16)*math.cos(row*np.pi*(2*y+1)/16)
            img_pixel[line, row] = n
    return np.ceil(img_pixel)
