#coding:utf-8
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

#打开图像，并转化成灰度图像
image = Image.open("photo.jpg").convert("L") 
image_array = np.array(image)

plt.subplot(2,1,1)
plt.imshow(image,cmap=cm.gray)
plt.axis("off")
plt.subplot(2,1,2)
plt.hist(image_array.flatten(),256) #flatten可以将矩阵转化成一维序列
plt.show()
