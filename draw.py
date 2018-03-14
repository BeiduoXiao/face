#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
#标签
labels = np.array(['3','5','6','3'])
#数据个数
dataLenth = 4
#数据
data = np.array([23,89,100,3])


angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) 
angles = np.concatenate((angles, [angles[0]])) 
 
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'ro-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title("pic", va='bottom')
ax.grid(True)
plt.show()