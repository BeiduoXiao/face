#coding:utf-8
from PIL import Image
import matplotlib.pyplot as pl
import numpy as np
import json
import fppapi
import hist_similar
import avg_similar
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




def lip(filepath):
    

    #导入模板
    springtem = Image.open('template/lip_tem_spring.jpg')
    summertem = Image.open('template/lip_tem_summer.jpeg')
    falltem = Image.open('template/lip_tem_fall.png')
    wintertem = Image.open('template/lip_tem_winter.jpeg')

    #导入被测试图片
    testim=lipcut(filepath)
    
    #得出与模板相似度
    avg_tem_sim=44.7548911322
    spring_similar_avg=avg_similar.similar(springtem,testim,avg_tem_sim)
    summer_similar_avg=avg_similar.similar(summertem,testim,avg_tem_sim)
    fall_similar_avg=avg_similar.similar(falltem,testim,avg_tem_sim)
    winter_similar_avg=avg_similar.similar(wintertem,testim,avg_tem_sim)
    
    '''
    hist_tem_sim=0.573661851093
    spring_similar_hist=hist_similar.similar(springtem,testim,hist_tem_sim)
    summer_similar_hist=hist_similar.similar(summertem,testim,hist_tem_sim)
    fall_similar_hist=hist_similar.similar(falltem,testim,hist_tem_sim)
    winter_similar_hist=hist_similar.similar(wintertem,testim,hist_tem_sim)
    
    '''
    #均值法结果集
    avg_result_list=[]
    avg_result_list.append(spring_similar_avg)
    avg_result_list.append(summer_similar_avg)
    avg_result_list.append(fall_similar_avg)
    avg_result_list.append(winter_similar_avg)
    
    '''
    #直方图相似度法结果集
    hist_result_list=[]
    hist_result_list.append(spring_similar_hist)
    hist_result_list.append(summer_similar_hist)
    hist_result_list.append(fall_similar_hist)
    hist_result_list.append(winter_similar_hist)
    
    '''


    



    print avg_result_list
    return avg_result_list
   
    
    


if __name__ == '__main__':
    filepath=r"testcases/lip_avg_better.jpg"
    lip(filepath)


