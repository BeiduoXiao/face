#coding:utf-8
from PIL import Image
import matplotlib.pyplot as pl
import numpy as np
import json
import fppapi
import hist_similar



def eyecut(filepath):

    apiresponse=fppapi.fppapi(filepath)
    get_dic=json.loads(apiresponse)
    face_list=get_dic['faces']
    #list[0] is dict
    list_dic=face_list[0]
    #keys of list_dic [u'landmark', u'attributes', u'face_token', u'face_rectangle']
    #'landmark' is a dict
    landmark_dic=list_dic['landmark']
    #keys of landmark_dic : all 83 landmarks https://www.faceplusplus.com.cn/landmarks/#demo
    upperleft=landmark_dic['left_eye_upper_left_quarter']
    lowerright=landmark_dic['left_eye_lower_right_quarter']
    

    upperleft_x=upperleft['x']
    upperleft_y=upperleft['y']
    
    lowerright_x=lowerright['x']
    lowerright_y=lowerright['y']



    im = Image.open(filepath)
    region = im.crop((upperleft_x, upperleft_y, lowerright_x, lowerright_y))
    #region是裁剪后的image对象
    return region

def randomization(hist):
    randomization_hist=[]
    
    for i in hist:
        ri=float(i)/2500
        randomization_hist.append(ri)

    return randomization_hist

#横坐标（灰度图像）
x=[]
for i in range(256):
    x.append(i)


#导入模板
springtem = Image.open('template/eye_tem_spring.jpg')
summertem = Image.open('template/eye_tem_summer.jpg')
falltem = Image.open('template/eye_tem_fall.jpg')
wintertem = Image.open('template/eye_tem_winter.jpg')


test = eyecut('testcases/eye_test_winter.jpeg')

size = (50,50)
springtem = springtem.resize(size).convert('L')
summertem = summertem.resize(size).convert('L')
falltem = falltem.resize(size).convert('L')
wintertem = wintertem.resize(size).convert('L')
test = test.resize(size).convert('L')



#产生直方图(测试用)
springtem_hisg=randomization(springtem.histogram())
summertem_hisg=randomization(summertem.histogram())
falltem_hisg=randomization(falltem.histogram())
wintertem_hisg=randomization(wintertem.histogram())
test_hisg=randomization(test.histogram())


linesummer, =pl.plot(x,summertem_hisg,color='green')
linefall, =pl.plot(x,falltem_hisg,color='red')
linespring, =pl.plot(x,springtem_hisg,color='yellow')
linewinter, =pl.plot(x,wintertem_hisg,color='black')
linetest, =pl.plot(x,test_hisg,color='blue')


l1 = pl.legend([linespring, linesummer,linefall,linewinter,linetest], ["SpringTemplate", "SummerTemplate","FallTemplate","WinterTemplate","TestImage"], loc=1)  
  

pl.gca().add_artist(l1)  

pl.show()