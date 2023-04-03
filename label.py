from dct import IDCT_block,DCT_block
from quantization import quantization,QF2Qtable_y
import numpy as np

def label(dct_blocks):
    l = len(dct_blocks)
    label = []
    for block in dct_blocks:
        i_block = IDCT_block(block) # i_block is pixel
        if (np.max(i_block) > 128 or np.min(i_block) < - 127): #溢出，则标1
            label.append(1)
        else :
            id_block = DCT_block(i_block) 
            #id_block：上一步还原出来的i_block再dct
            #idq_block:id_block再经过量化，若idq_block != block,则标1
            idq_block = quantization(id_block,Q=QF2Qtable_y(QF= 71))
            if not np.array_equal(idq_block,block): 
                label.append(1)
            else:
                print('robust block')
                label.append(0)
    return label
