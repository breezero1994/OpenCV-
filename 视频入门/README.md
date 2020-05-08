# 目标
学习读取视频，显示视频和保存视频。  
学习从相机捕捉并显示它。  
你将学习以下功能：cv.VideoCapture()，cv.VideoWriter()  
## 从相机中读取视频
通常情况下，我们必须用摄像机捕捉实时画面。提供了一个非常简单的界面。让我们从摄像头捕
捉一段视频(我使用的是我笔记本电脑内置的网络摄像头) ，将其转换成灰度视频并显示出来。只是
一个简单的任务开始。  
要捕获视频，你需要创建一个 VideoCapture 对象。它的参数可以是设备索引或视频文件的名
称。设备索引就是指定哪个摄像头的数字。正常情况下，一个摄像头会被连接(就像我的情况一
样)。所以我简单地传0(或-1)。你可以通过传递1来选择第二个相机，以此类推。在此之后，你可以
逐帧捕获。但是在最后，不要忘记释放俘虏。
```
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
        # 我们在框架上的操作到这里
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 显示结果帧e
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
# 完成所有操作后，释放捕获器
cap.release()
cv.destroyAllWindows()
```
cap.read() 返回布尔值( True / False )。如果正确读取了帧，它将为 True 。因此，你可以通过检查此返回值来检查视频的结尾。  
有时，cap可能尚未初始化捕获。在这种情况下，此代码显示错误。你可以通过**cap.isOpened**()方法检查它是否已初始化。如果是 True ，那么确定。否则，使用
**cap.open**()打开它。  
你还可以使用 cap.get(propId) 方法访问该视频的某些功能，其中propId是0到18之间的一个数字。每个数字表示视频的属性（如果适用于该视频），并且可以显示完整的详细信息在这里看到：cv::VideoCapture::get()。其中一些值可以使用 cap.set(propId，value) 进行修改。 value是你想要的新值。  
例如，我可以通过 cap.get(cv.CAP_PROP_FRAME_WIDTH) 和 cap.get(cv.CAP_PROP_FRAME_HEIGHT)检查框架的宽度和高度。默认情况下，它的分辨率为640x480。但我想将其修改为320x240。只需使用和即可。 ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320) and ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,240).  

