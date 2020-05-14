# 目标
* 学习图像的几种算术运算，例如加法，减法，按位运算等。
* 您将学习以下功能：cv.add，**cv.addWeighted**等。
## 图像加法
您可以通过OpenCV函数 cv.add() 或仅通过numpy操作 res = img1 + img2 添加两个图像。两个图像应具有相同的深度和类型，或者第二个图像可以只是一个标量值。
### 注意
OpenCV加法和Numpy加法之间有区别。OpenCV加法是饱和运算，而Numpy加法是模运算。
例如，考虑以下示例：
```
x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y) ) # 250+10 = 260 => 255
[[255]]
print( x+y ) # 250+10 = 260 % 256 = 4
[4]
```
当添加两个图像时，它将更加可见。OpenCV功能将提供更好的结果。因此，始终最好坚持使用
OpenCV功能
## 图像融合
这也是图像加法，但是对图像赋予不同的权重，以使其具有融合或透明的感觉。根据以下等式添
加图像：
G(x)= (1 - \alpha)f_0(x)+ \alpha f_1(x)
通过从 \alpha 从 0\rightarrow1 更改，您可以在一个图像到另一个图像之间执行很酷的过渡。
在这里，我拍摄了两个图像，将它们融合在一起。第一幅图像的权重为0.7，第二幅图像的权重为
0.3。 cv.addWeighted() 在图像上应用以下公式。
dst=\alpha \cdot img1+\beta \cdot img2 + \gamma
在这里，\gamma 被视为零。
```
img1 = cv.imread('ml.png')
img2 = cv.imread('opencv-logo.png')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()
```



