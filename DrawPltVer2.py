# -*- coding: utf-8 -*-
import os
import platform
import sys
import requests
#添加matplotlib.use('TkAgg')不然Mac无法show图片
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
print(sys.getdefaultencoding())


font = {'family': 'sans-serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 16,
        }


def DrawPlt2(filePath):
    plt.figure(num = 1, figsize = (15, 15), dpi = 100)
    ax = plt.gca()
    #x轴方向调整：
    ax.xaxis.set_ticks_position('top') #将x轴的位置设置在顶部
    ax.invert_xaxis() #x轴反向
    
    #y轴方向调整：
    ax.yaxis.set_ticks_position('right') #将y轴的位置设置在右边
    ax.invert_yaxis() #y轴反向

    #Mac格式
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    tempPath = os.path.basename(filePath)
    fileName = os.path.splitext(tempPath)[0]
    contents = file.read()

    bDown = False
    pointX = []
    pointY = []
    for coordinate in contents.split():
        print(coordinate)
        if (coordinate[0] == 'U'):
            coordinate = coordinate.strip('U')
            coordinate = coordinate.split(',', 1)
            pointX.append(int(coordinate[0]))
            pointY.append(int(coordinate[1]))
            bDown = False
        elif (coordinate[0] == 'D'):
            coordinate = coordinate.strip('D')
            coordinate = coordinate.split(',', 1)
            pointX.append(int(coordinate[0]))
            pointY.append(int(coordinate[1]))
            bDown = True
        else:
            continue

        if len(pointX) > 1 :       
            if bDown:
                plt.plot(pointX, pointY, color = "r")
                del pointX[0]
                del pointY[0]
            else:
                plt.plot(pointX, pointY, linestyle = 'dotted', color = "b")
                del pointX[0]
                del pointY[0]
        else:
            continue
       
    
      # 设置图表标题并给坐标轴加上标签
    plt.title("V2", fontsize = 18)

    plt.xlabel("X", font)
    plt.ylabel("Y", font)

    
     # 设置 图例所在的位置 使用推荐位置
    plt.legend(loc = 'best') 

    plt.axis("equal")
    # toggle fullscreen mode
    #plt.get_current_fig_manager().full_screen_toggle() 
    plt.show() 
    #保存图象
    #plt.savefig('test11111.pdf')
    plt.close()

if __name__ == "__main__":
    filePath = '/Users/zhoujunliang/Downloads/aaa.plt'
    DrawPlt2(filePath)