
import numpy as np

def RGB2YUV420(image):
    h, w, c = image.shape
    image_y = np.zeros((h, w), dtype=np.uint8)
    image_u = np.zeros(((h-1)//2+1, (w-1)//2+1), dtype=np.uint8)
    image_v = np.zeros(((h-1)//2+1, (w-1)//2+1), dtype=np.uint8)
    for line in range(h):
        for row in range(w):
            B = image[line, row, 0]
            G = image[line, row, 1]
            R = image[line, row, 2]
            Y = np.round(0.299*R + 0.587*G + 0.114*B) 
            image_y[line, row] = Y
            if line % 2 == 0 and row % 2 == 0:
                U = np.round(0.5*R - 0.4187*G - 0.0813*G ) + 128
                image_u[line//2, row//2] = U 
            if line % 2 == 1 or line == h-1:
                V = np.round(-0.1687*R - 0.3313*G + 0.5*B ) + 128
                image_v[line//2, row//2] = V
    return image_y, image_u, image_v
