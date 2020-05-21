# 目标
* 在本教程中，你将学习如何将图像从一个色彩空间转换到另一个，像BGR↔灰色，BGR↔HSV等
* 除此之外，我们还将创建一个应用程序，以提取视频中的彩色对象
* 你将学习以下功能：cv.cvtColor，**cv.inRange**等。
# 改变颜色空间
OpenCV中有超过150种颜色空间转换方法。但是我们将研究只有两个最广泛使用的,BGR↔灰色和BGR↔HSV。  
对于颜色转换，我们使用cv函数。cvtColor(input_image, flag)，其中flag决定转换的类型。  
对于BGR→灰度转换，我们使用标志cv.COLOR_BGR2GRAY。类似地，对于BGR→HSV，我们使用标志cv.COLOR_BGR2HSV。要获取其他标记，只需在Python终端中运行以下命令:
```Python
import cv2 as cv
flags = [i for i in dir(cv) if i.startwith('COLOR_')]
print(flags)
```
## 注意
HSV的色相范围为[0,179]，饱和度范围为[0,255]，值范围为[0,255]。不同的软件使用不同的规模。因此，如果你要将OpenCV值和它们比较，你需要将这些范围标准化。
