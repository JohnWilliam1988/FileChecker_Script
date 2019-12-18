
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#import numpy as np
import sys
print(sys.getdefaultencoding())

#def FindAllPltFiles(Dirpath):

Coordinates_X = []
Coordinates_Y = []

#Mac格式
file = open(r'华为 荣耀 畅玩 7 前膜 1113.plt', encoding='utf-8')
print("文件名为： " + file.name)
contents = file.read()
print(contents)
for coordinate in contents.split():
    #print(coordinate)
    if (coordinate[0] == 'D'):
        coordinate = coordinate.strip('D')
        print(coordinate)
        coordinate = coordinate.split(',', 1)
        print(coordinate[0])
        print(coordinate[1])
        Coordinates_X.append(int(coordinate[0]))
        Coordinates_Y.append(int(coordinate[1]))


print(Coordinates_X)
print(Coordinates_Y)
 
# p1=[0,1.1,1.8,3.1,4.0]  # 数据点
# p2=[2,2.4,4.3,3.5,2.5]
 
#创建绘图图表对象，可以不显式创建，跟cv2中的cv2.namedWindow()用法差不多
# plt.figure('Draw')
 
# plt.plot(Coordinates_X, Coordinates_Y, 'ro')
 
#plt.draw()  # 显示绘图

plt.scatter(Coordinates_X, Coordinates_Y, s = 2)

# 设置图表标题并给坐标轴加上标签
plt.title(file.name, fontsize = 24)
plt.xlabel('X', fontsize = 14)
plt.ylabel('Y', fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.plot(Coordinates_X, Coordinates_Y, 'ob')
# 设置每个坐标轴的取值范围
plt.axis([0, 10000, 0, 8000]) 
plt.legend(loc = 'best')    # 设置 图例所在的位置 使用推荐位置
#plt.show()
 
 #保存图象
plt.savefig('SavdJpg/' + file.name + '.jpg')
 
plt.close()
