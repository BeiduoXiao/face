#coding:utf-8
# 导入第三方模块

import numpy as np
import matplotlib.pyplot as plt
import sys
from PIL import Image
import os


def radar_part(lip,skin,brow,eye):
    
    reload(sys)
    sys.setdefaultencoding('utf-8')


    plt.rcParams['axes.unicode_minus'] = False

    # 使用ggplot的绘图风格
    plt.style.use('ggplot')

    # 构造数据
    values = lip
    values2 = skin
    values3= brow
    values4= eye
    feature = ['SPRING','SUMMER','FALL','WINTER']

    N = len(values)
    # 设置雷达图的角度，用于平分切开一个圆面
    angles=np.linspace(0, 2*np.pi, N, endpoint=False)
    # 为了使雷达图一圈封闭起来，需要下面的步骤
    values=np.concatenate((values,[values[0]]))
    values2=np.concatenate((values2,[values2[0]]))
    values3=np.concatenate((values3,[values3[0]]))
    values4=np.concatenate((values4,[values4[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    # 绘图
    fig=plt.figure()
    ax = fig.add_subplot(111, polar=True)
    # 绘制折线图
    ax.plot(angles, values, 'o-', linewidth=2, label = 'LIP')
    # 填充颜色
    ax.fill(angles, values, alpha=0.25)
    # 绘制第二条折线图
    ax.plot(angles, values2, 'o-', linewidth=2, label = 'SKIN')
    ax.fill(angles, values2, alpha=0.25)
    #第三条
    ax.plot(angles, values3, 'o-', linewidth=2, label = 'BROW')
    ax.fill(angles, values3, alpha=0.25)
    #第四条
    ax.plot(angles, values4, 'o-', linewidth=2, label = 'EYE')
    ax.fill(angles, values4, alpha=0.25)
    # 添加每个特征的标签
    ax.set_thetagrids(angles * 180/np.pi, feature)
    # 设置雷达图的范围
    ax.set_ylim(0,1)
    # 添加标题
    plt.title('Seasonal Types of Sub-regions')

    # 添加网格线
    ax.grid(True)
    # 设置图例
    plt.legend(loc = 'best')
    # 显示图形
    
    plt.savefig("radar_part.png")
    

def radar_total(total):
    
    reload(sys)
    sys.setdefaultencoding('utf-8')


    plt.rcParams['axes.unicode_minus'] = False

    # 使用ggplot的绘图风格
    plt.style.use('ggplot')

    # 构造数据
    values = total
    #构造展示标签
    spring='SPRING'+'\n'+'%s'%(total[0])
    summer='SUMMER'+'\n'+'%s'%(total[1])
    fall='FALL'+'\n'+'%s'%(total[2])
    winter='WINTER'+'\n'+'%s'%(total[3])
    feature = [spring,summer,fall,winter]

    N = len(values)
    # 设置雷达图的角度，用于平分切开一个圆面
    angles=np.linspace(0, 2*np.pi, N, endpoint=False)
    # 为了使雷达图一圈封闭起来，需要下面的步骤
    values=np.concatenate((values,[values[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    # 绘图
    fig=plt.figure()
    ax = fig.add_subplot(111, polar=True)
    # 绘制折线图
    ax.plot(angles, values, 'o-', linewidth=2, label = 'OVERALL')
    # 填充颜色
    ax.fill(angles, values, alpha=0.25)
    # 添加每个特征的标签
    ax.set_thetagrids(angles * 180/np.pi, feature)
    # 设置雷达图的范围
    ax.set_ylim(0,1)
    # 添加标题
    plt.title('Overall Season Type')

    # 添加网格线
    ax.grid(True)
    # 设置图例
    plt.legend(loc = 'best')
    # 显示图形
    
    plt.savefig("radar_total.png")

    

if __name__ == '__main__':
    
    lip=[0.1,0.2,0.33682678,0.45678678]
    skin=[0.588767678,0.6117568736,0.7353567,0.82363808]
    brow=[0.922333434,0.79262827,0.7235356,0.12336808]
    eye=[0.1237987678,0.3417568736,0.2353567,0.6282663808]
    total=[0.006271069,0.725892122,0.152535612,0.089646741]
    radar_total(total)
    radar_part(lip,skin,brow,eye)