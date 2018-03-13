#coding:utf-8
from PIL import Image
import matplotlib.pyplot as pl
import numpy as np
import lipcut

x=[]
for i in range(256):
    x.append(i)


path1=r"wintertest.jpg"
path2=r"falltest.jpg"
path3=r"summertest.jpg"
path4=r"test.jpg"
path5=r"summertemplate-s.png"
size = (50,50)

image1=lipcut.lipcut(path1)
image2=lipcut.lipcut(path2)
image3=lipcut.lipcut(path3)
image4=lipcut.lipcut(path4)
image5=lipcut.lipcut(path5)


image1 = image1.resize(size).convert("L")
g = image1.histogram()
image2 = image2.resize(size).convert("L")
s = image2.histogram()
image3=image3.resize(size).convert("L")
l3=image3.histogram()
image4=image4.resize(size).convert("L")
l4=image4.histogram()
image5=image5.resize(size).convert("L")
l5=image5.histogram()

pl.plot(x,g,color='green')
pl.plot(x,s,color='red')
pl.plot(x,l3,color='yellow')
pl.plot(x,l4,color='black')
pl.plot(x,l5,color='blue')

pl.show()
image1.show()
image2.show()
image3.show()
image4.show()
	

