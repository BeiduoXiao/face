#coding:utf-8
#灰度均值+欧氏距离

import numpy as np
from PIL import Image
import matplotlib.pyplot as pl




def similar(image1,image2,tem_sim):
    
    
    
    #大小及灰度处理
    size = (50,50)
    image1 = image1.resize(size).convert('L')
    image2 = image2.resize(size).convert('L')
    

    #产生频数直方图
    
    image1_hist=image1.histogram()
    image2_hist=image2.histogram()
    
    
    
    
    
    #value：频率值 key：下标（灰度值）
    key1=[]
    value1=[]
    #image1的平均灰度值
    gl_sum1=0
    
    for i in image1_hist:
        if i>=(2500*0.010):
            value1.append(i)
            key1.append(image1_hist.index(i))
        else:
            continue

    
    for i in key1:
        gl_sum1=gl_sum1+(i*value1[key1.index(i)])

    gl_avg1=float(gl_sum1)/sum(value1)


    
   
    key2=[]
    value2=[]
    #image2的平均灰度值
    gl_sum2=0
    
    for i in image2_hist:
        if i>=(2500*0.010):
            value2.append(i)
            key2.append(image2_hist.index(i))
        else:
            continue

    
    for i in key2:
        gl_sum2=gl_sum2+(i*value2[key2.index(i)])

    gl_avg2=float(gl_sum2)/sum(value2)
    
    avg_diff=abs(gl_avg1-gl_avg2)
    
    #灰度差/模板最小差值
    
    #我们认为差tem_sim灰度值就不属于同一季节了
    #tem_sim=44.7548911322

    avg_similar=1-(avg_diff/tem_sim)

    if avg_similar<0:
        avg_similar=0
    else:
        avg_similar=avg_similar
    
    
    return avg_similar
    #print avg_similar
    
    #print gl_avg1
    #print gl_avg2

    
        
    
if __name__ == '__main__':
    #filepath=r"testcases/lip_test_winter2.jpeg"
    #springtem = Image.open('template/lip_tem_spring6.jpg')
    #summertem = Image.open('template/lip_tem_summer.jpeg')
    #falltem = Image.open('template/lip_tem_fall.jpg')
    #wintertem = Image.open('template/lip_tem_winter.jpeg')
    #testim=Image.open(filepath)
    Image1= Image.open('template/eye_tem_winter.jpg')
    Image2= Image.open('template/brow_tem_fall.jpg')
    
    tem_sim=44.7548911322
    similar(Image1,Image2,tem_sim)







