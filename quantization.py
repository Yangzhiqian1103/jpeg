import numpy as np

def quantization(blocks, Q):
    #用量化表Q处理 由DCT block组成的列表，返回量化DCT block组成的列表。
    img_quan = []
    for block in blocks:
        img_quan.append((np.round(np.divide(block, Q))).astype(np.uint8))
    return img_quan

#JPEG算法提供了两张标准化系数矩阵，分别处理亮度数据和色差数据，Q_table_basic 表示 QF =50 的图像质量。

def QF2Qtable_c(QF) :
    # Q_c 色差数据量化表
    block_size = 8
    Q_table_basic =[[17,18,24,47,99,99,99,99],[18,21,26,66,99,99,99,99],[24,26,56,99,99,99,99,99],[47,66,99,99,99,99,99,99],[99,99,99,99,99,99,99,99],[99,99,99,99,99,99,99,99],[99,99,99,99,99,99,99,99],[99,99,99,99,99,99,99,99]]
    Q_table = np.zeros_like(Q_table_basic,dtype=np.uint8)
    if QF == 50:
        return Q_table_basic
    if QF > 50:
        for i in range(block_size):
            for j in range(block_size):
                Q_table[i][j] = np.round(Q_table_basic[i][j]*((100-QF)/50))
    if QF < 50:
        for i in range(block_size):
            for j in range(block_size):
                Q_table[i][j] = np.round(Q_table_basic[i][j]*(50/QF))
    return Q_table

def QF2Qtable_y(QF):
    # Q_Y 亮度数据量化表
    block_size = 8
    Q_table_basic = [[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56],[14,17,22,29,51,87,80,62],[18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92],[49,64,78,87,103,121,120,101],[72,92,95,98,112,100,103,99]]
    Q_table = np.zeros_like(Q_table_basic,dtype=np.uint8)

    if QF == 50:
        return Q_table_basic
    if QF > 50:
        for i in range(block_size):
            for j in range(block_size):
                Q_table[i][j] = np.round(Q_table_basic[i][j]*((100-QF)/50))
    if QF < 50:
        for i in range(block_size):
            for j in range(block_size):
                Q_table[i][j] = np.round(Q_table_basic[i][j]*(50/QF))
    return Q_table