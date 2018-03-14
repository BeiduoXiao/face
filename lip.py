#coding:utf-8
from PIL import Image
import matplotlib.pyplot as pl
import numpy as np
import json
import fppapi
import hist_similar
#注：所有的filepath为filepath = r"photo.jpg"格式


#返回裁剪出的嘴唇image对象
def lipcut(filepath):

    apiresponse=fppapi.fppapi(filepath)
    get_dic=json.loads(apiresponse)
    face_list=get_dic['faces']
    #list[0] is dict
    list_dic=face_list[0]
    #keys of list_dic [u'landmark', u'attributes', u'face_token', u'face_rectangle']
    #'landmark' is a dict
    landmark_dic=list_dic['landmark']
    #keys of landmark_dic : all 83 landmarks https://www.faceplusplus.com.cn/landmarks/#demo
    upperleft=landmark_dic['mouth_upper_lip_left_contour2']
    lowerright=landmark_dic['mouth_lower_lip_right_contour3']
    

    upperleft_x=upperleft['x']
    upperleft_y=upperleft['y']
    
    lowerright_x=lowerright['x']
    lowerright_y=lowerright['y']



    im = Image.open(filepath)
    region = im.crop((upperleft_x, upperleft_y, lowerright_x, lowerright_y))
    #region是裁剪后的image对象
    return region

#数值直方图转化为频率分布直方图
def randomization(hist):
    randomization_hist=[]
    
    for i in hist:
        ri=float(i)/2500
        randomization_hist.append(ri)

    return randomization_hist


def main(filepath):
    
    #横坐标（灰度图像）
    x=[]
    for i in range(256):
        x.append(i)

    #导入模板
    springtem = Image.open('template/lip_tem_spring.jpeg')
    summertem = Image.open('template/lip_tem_summer.jpeg')
    falltem = Image.open('template/lip_tem_fall.jpg')
    wintertem = Image.open('template/lip_tem_winter.jpeg')

    
    #导入被测试图片
    testim=lipcut(filepath)

    #大小及灰度处理
    size = (50,50)
    springtem = springtem.resize(size).convert('L')
    summertem = summertem.resize(size).convert('L')
    falltem = falltem.resize(size).convert('L')
    wintertem = wintertem.resize(size).convert('L')
    
    testim = testim.resize(size).convert('L')

    #产生直方图
    
    springtem_hisg=randomization(springtem.histogram())
    summertem_hisg=randomization(summertem.histogram())
    falltem_hisg=randomization(falltem.histogram())
    wintertem_hisg=randomization(wintertem.histogram())

    testim_hisg=randomization(testim.histogram())
    
    #得出与模板相似度
    spring_similar=hist_similar.cal(springtem_hisg,testim_hisg)
    summer_similar=hist_similar.cal(summertem_hisg,testim_hisg)
    fall_similar=hist_similar.cal(falltem_hisg,testim_hisg)
    winter_similar=hist_similar.cal(wintertem_hisg,testim_hisg)

    #pl.plot(x,summertem_hisg,color='green')
    #pl.plot(x,falltem_hisg,color='red')
    #pl.plot(x,springtem_hisg,color='yellow')
    #pl.plot(x,wintertem_hisg,color='black')
    #pl.plot(x,testim_hisg,color='blue')
    #pl.show()
    
    print spring_similar
    print summer_similar
    print fall_similar
    print winter_similar



if __name__ == '__main__':
    filepath=r"testcases/lip_test_summer6.jpeg"
    main(filepath)


