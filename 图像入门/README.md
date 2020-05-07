# 目标
在这里，你将学习如何读取图像，如何显示图像以及如何将其保存回去
你将学习以下功能：cv.imread(), cv.imshow(), cv.imwrite()
（可选）你将学习如何使用Matplotlib显示图像
使用OpenCV
读取图像
使用**cv.imread**()函数读取图像。图像应该在工作目录或图像的完整路径应给出。
第二个参数是一个标志，它指定了读取图像的方式。
  cv.IMREAD_COLOR：加载彩色图像。任何图像的透明度都会被忽视。它是默认标志。
  cv.IMREAD_GRAYSCALE：以灰度模式加载图像
  cv.IMREAD_UNCHANGED：加载图像，包括alpha通道
注意除了这三个标志，你可以分别简单地传递整数1、0或-1。
