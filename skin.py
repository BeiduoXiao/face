#coding:utf-8
from PIL import Image
import matplotlib.pyplot as pl
import numpy as np
import json
import fppapi
import hist_similar
import avg_similar
#注：所有的filepath为filepath = r"photo.jpg"格式

#返回裁剪出的皮肤image对象
def skincut(filepath):

    apiresponse=fppapi.fppapi(filepath)
    get_dic=json.loads(apiresponse)
    face_list=get_dic['faces']
    #list[0] is dict
    list_dic=face_list[0]
    #keys of list_dic [u'landmark', u'attributes', u'face_token', u'face_rectangle']
    #'landmark' is a dict
    landmark_dic=list_dic['landmark']
    #keys of landmark_dic : all 83 landmarks https://www.faceplusplus.com.cn/landmarks/#demo
    upperleft=landmark_dic['nose_right']
    lowerright=landmark_dic['contour_right5']
    

    upperleft_x=upperleft['x']
    upperleft_y=upperleft['y']
    
    lowerright_x=lowerright['x']
    lowerright_y=lowerright['y']



    im = Image.open(filepath)
    region = im.crop((upperleft_x, upperleft_y, lowerright_x, lowerright_y))
    #region是裁剪后的image对象
    return region




def skin(filepath):
    

    #导入模板
    springtem = Image.open('template/skin_tem_spring.jpeg')
    summertem = Image.open('template/skin_tem_summer.jpeg')
    falltem = Image.open('template/skin_tem_fall.jpg')
    wintertem = Image.open('template/skin_tem_winter.jpeg')

    #导入被测试图片
    testim=skincut(filepath)

    #得出与模板相似度
    avg_tem_sim=32.160981422
    
    spring_similar_avg=avg_similar.similar(springtem,testim,avg_tem_sim)
    summer_similar_avg=avg_similar.similar(summertem,testim,avg_tem_sim)
    fall_similar_avg=avg_similar.similar(falltem,testim,avg_tem_sim)
    winter_similar_avg=avg_similar.similar(wintertem,testim,avg_tem_sim)


    #均值法结果集
    avg_result_list=[]
    avg_result_list.append(spring_similar_avg)
    avg_result_list.append(summer_similar_avg)
    avg_result_list.append(fall_similar_avg)
    avg_result_list.append(winter_similar_avg)



    


    #print avg_result_list
    
    return avg_result_list


if __name__ == '__main__':
    filepath=r"testcases/skin_test_fall.jpg"
    skin(filepath)


