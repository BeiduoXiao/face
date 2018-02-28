#coding:utf-8
import fppapi
import json
#json->dic
get_dic=json.loads(fppapi.qrcont)
face_list=get_dic['faces']
#list[0] is dict
list_dic=face_list[0]
#keys of list_dic [u'landmark', u'attributes', u'face_token', u'face_rectangle']
#'landmark' is a dict
landmark_dic=list_dic['landmark']
#keys of landmark_dic : all 83 landmarks https://www.faceplusplus.com.cn/landmarks/#demo
lefteye_center=landmark_dic['left_eye_center']

coordinate_x=lefteye_center['x']
coordinate_y=lefteye_center['y']
#print coordinate_x
#print coordinate_y


