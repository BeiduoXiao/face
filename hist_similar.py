#coding:utf-8


import numpy as np



def cal(hist1,hist2):
    p=np.asarray(hist1)
    q=np.array(hist2)
    #巴氏系数
    BC=np.sum(np.sqrt(p*q))

    #Hellinger距离：
    #h=np.sqrt(1-BC)

    #巴氏距离：
    #b=-np.log(BC)
    
    return BC





'''
def hist_similar(lh, rh):

    assert len(lh) == len(rh)

    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)
'''