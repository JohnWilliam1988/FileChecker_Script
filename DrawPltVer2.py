# -*- coding: utf-8 -*-
import os
import sys
#添加matplotlib.use('TkAgg')不然Mac无法show图片
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
print(sys.getdefaultencoding())
#中文显示
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

font = {'family': 'sans-serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 16,
        }


#@filePath plt路径
#@bPlotUp 是否绘制提刀路径
#@原点位置0,1,2,3 顺时针对应左上、右上、右下、左下四个位置
def Draw(filePath, bPlotUp = True, originPos = 0):
    plt.figure(num = 1, figsize = (15, 15), dpi = 100)
    ax = plt.gca()
    title = ''
    if (originPos == 0):
        ax.xaxis.set_ticks_position('top')
        ax.yaxis.set_ticks_position('left')
        ax.invert_yaxis() 
        title = 'origin pos top-left'
    elif (originPos == 1):
        ax.xaxis.set_ticks_position('top')
        ax.yaxis.set_ticks_position('right') 
        ax.invert_xaxis()
        ax.invert_yaxis() 
        title = 'origin pos top-right'
    elif (originPos == 2):
        ax.xaxis.set_ticks_position('bottom') 
        ax.yaxis.set_ticks_position('right') 
        ax.invert_xaxis() 
        title = 'origin pos bottom-right'
    elif (originPos == 3):
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        title = 'origin pos bottom-left'

    #Mac格式
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    tempPath = os.path.basename(filePath)
    fileName = os.path.splitext(tempPath)[0]
    contents = file.read()

    bDown = False
    #因为这里需要确保是D里面的坐标数据
    minX, minY, maxX, maxY = 10000, 10000, -1000, -1000
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

            #获取最大最小值，用于计算宽高
            if (minX > int(coordinate[0])):
                minX = int(coordinate[0])
            if (maxX < int(coordinate[0])):
                maxX = int(coordinate[0])
            if (minY > int(coordinate[1])):
                minY = int(coordinate[1])
            if (maxY < int(coordinate[1])):
                maxY = int(coordinate[1])

        else:
            continue

        #有两个点才能进行绘制
        if len(pointX) > 1 :      
            #绘制切割运动轨迹 
            if bDown:
                plt.plot(pointY, pointX, color = "r", linewidth = 1)
            #绘制提刀运动轨迹
            else:
                if bPlotUp:
                    plt.plot(pointY, pointX, linestyle = 'dashdot', color = "b", linewidth = 0.25)

            #删除前一个点
            del pointX[0]
            del pointY[0]
        else:
            continue
       
    
    # 设置图表标题并给坐标轴加上标签
    plt.title(title, fontsize = 18)
    print(minX, maxX, minY, maxY)
    plt.xlabel(str((maxY - minY) / 40) + "mm", font)
    plt.ylabel(str((maxX - minX) / 40) + "mm", font)

    
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
    Draw(filePath, True, 0)