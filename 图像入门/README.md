# 目标
* 在这里，你将学习如何读取图像，如何显示图像以及如何将其保存回去  
* 你将学习以下功能：cv.imread(), cv.imshow(), cv.imwrite()  
* （可选）你将学习如何使用Matplotlib显示图像  

# 使用OpenCV
## 读取图像
使用**cv.imread**()函数读取图像。图像应该在工作目录或图像的完整路径应给出。  
第二个参数是一个标志，它指定了读取图像的方式。  
* cv.IMREAD_COLOR：加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。  
* cv.IMREAD_GRAYSCALE：以灰度模式加载图像  
* cv.IMREAD_UNCHANGED：加载图像，包括alpha通道  
注意除了这三个标志，你可以分别简单地传递整数1、0或-1。  

## 请参见下面的代码：
```Ｐｙｔｈｏｎ
import numpy as np　　
import cv2 as cv
```
### 加载彩色灰度图像
```Ｐｙｔｈｏｎ
img = cv.imread('GEM.jpg'，0)
```
即使图像路径错误，它也不会引发任何错误，但是print(img)会给出None

## 显示图像
使用函数**cv.imshow()**在窗口中显示图像。窗口自动适合图像尺寸。  
第一个参数是窗口名称，它是一个字符串。第二个参数是我们的对象。你可以根据需要创建任意
多个窗口，但可以使用不同的窗口名称。  
```Ｐｙｔｈｏｎ
cv.imshow('image'，img）
cv.waitKey(0)
cv.destroyAllWindows()
```

## 写入图像
使用函数**cv.imwrite**()保存图像。  
第一个参数是文件名，第二个参数是要保存的图像。 cv.imwrite('GEM.png'，img)
这会将图像以PNG格式保存在工作目录中。
### 总结
在下面的程序中，以灰度加载图像，显示图像，按s保存图像并退出，或者按ESC键直接退出而不保存。

## 使用Matplotlib
Matplotlib是Python的绘图库，可为你提供多种绘图方法。你将在接下来的文章中看到它们。在这
里，你将学习如何使用Matplotlib显示图像。你可以使用Matplotlib缩放图像，保存图像等。

```
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 隐藏 x 轴和 y 轴上的刻度值
plt.show()
```

