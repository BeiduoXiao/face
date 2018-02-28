#coding=utf-8
import getcoordinate
import fppapi

from PIL import Image

#打开要处理的图像
img_src = Image.open('photo.jpg')

#转换图片的模式为RGBA
img_src = img_src.convert('RGBA')

#获得文字图片的每个像素点
src_strlist = img_src.load()
#100,100 是像素点的坐标
coordinate_x=getcoordinate.coordinate_x
coordinate_y=getcoordinate.coordinate_y

data = src_strlist[coordinate_x,coordinate_y]
#结果data是一个元组包含这个像素点的颜色信息
print data
