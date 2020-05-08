# 函数imread(), imshow(), imwrite()

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 图像读取：函数imread()
# 第一个分量是图像所在的路径
# 第二个分量是读取的形式
img = cv.imread('GEM.jpg', 0)

# 图像保存：函数imwite()
# 第一个分量是图像所要存储的路径和格式
# 第二个分量是图像像素值组成的矩阵
cv.imwrite('GEM.png', img)

# 图像显示：函数imshow()
# 第一个分量是图像的名字
# 第二个分量是图像像素值组成的矩阵
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()


# 图像显示：函数plt.imshow()
##plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
##plt.xticks([]), plt.yticks([]) # 隐藏 x 轴和 y 轴上的刻度值
##plt.show()

# 批量加注释Alt+3
# 批量去注释Alt+4
