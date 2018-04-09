#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt




def draw(result_list,p):
    
    datalist=[]
    for i in result_list:
        i=round(i,2)
        i=int(i*100)
        i=i-30
        if i<0:
            i=0
        else:
            i=i
        datalist.append(i)

    #标签
    labels = np.array(['Spring','Summer','Fall','Winter'])
    #数据个数
    dataLenth = 4
    #数据
    data = np.array(datalist)


    angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
    data = np.concatenate((data, [data[0]])) 
    angles = np.concatenate((angles, [angles[0]])) 
    
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'ro-', linewidth=2)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    ax.set_title("part: %s", va='bottom')%(p)
    ax.grid(True)
    plt.show()
    return fig


    

if __name__ == '__main__':
   
    result_list=[0.789266205454602, 0.9061880420024436, 0.8838422369872387, 0.31063851015226257]
    s="eye"
    draw(result_list,s)