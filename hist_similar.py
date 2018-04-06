#coding:utf-8
#巴氏系数比较全直方图拟合程度

import numpy as np
from PIL import Image


#数值直方图转化为频率分布直方图
def randomization(hist):
    randomization_hist=[]
    
    for i in hist:
        ri=float(i)/2500
        randomization_hist.append(ri)

    return randomization_hist

def similar(image1,image2,tem_sim):
    #大小及灰度处理
    size = (50,50)
    image1 = image1.resize(size).convert('L')
    image2 = image2.resize(size).convert('L')
    

    #产生频率直方图
    
    image1_hist=randomization(image1.histogram())
    image2_hist=randomization(image2.histogram())
    
    #巴氏系数法计算两频率曲线拟合程度
    p=np.asarray(image1_hist)
    q=np.array(image2_hist)
    #巴氏系数BC
    BC=np.sum(np.sqrt(p*q))
    print BC
    #巴氏系数法结果集处理（减去最大模板相似度）
    
    #tem_sim=0.573661851093
    
    if BC>tem_sim:
        BC=round(((BC-tem_sim)/(1-tem_sim)),2)
    else:
        BC=0.00
    
  
    
    
    return BC




if __name__ == '__main__':
    Image1= Image.open('template/lip_tem_fall.png')
    Image2= Image.open('template/lip_tem_summer.jpeg')
    tem_sim=0.573661851093
    
    similar(Image1,Image2,tem_sim)
    




