# -*- coding: utf-8 -*-
import os
import sys
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


def Draw(filePath):
    plt.figure(num = 1, figsize = (15, 15), dpi = 100)
    ax = plt.gca()
    #x轴方向调整：
    ax.xaxis.set_ticks_position('top') #将x轴的位置设置在顶部
    # ax.invert_xaxis() #x轴反向
    
    #y轴方向调整：
    # ax.yaxis.set_ticks_position('left') #将y轴的位置设置在右边
    ax.invert_yaxis() #y轴反向

    #Mac格式
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    tempPath = os.path.basename(filePath)
    fileName = os.path.splitext(tempPath)[0]
    contents = file.read()

    bDown = False
    minX, minY, maxX, maxY = 0, 0, 0, 0
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

            if (int(coordinate[0]) < minX):
                minX = int(coordinate[0])
            if (int(coordinate[0]) > maxX):
                maxX = int(coordinate[0])
            if (int(coordinate[1]) < minY):
                minY = int(coordinate[1])
            if (int(coordinate[1]) > maxY):
                maxY = int(coordinate[1])
        else:
            continue

        #有两个点才能进行绘制
        if len(pointX) > 1 :       
            #绘制提刀运动轨迹
            if bDown:
                plt.plot(pointY, pointX, color = "r", linewidth = 1)
            #绘制切割运动轨迹
            else:
                plt.plot(pointY, pointX, linestyle = 'dotted', color = "b", linewidth = 1)

            #删除前一个点
            del pointX[0]
            del pointY[0]
        else:
            continue
       
    
      # 设置图表标题并给坐标轴加上标签
    plt.title("V2", fontsize = 18)

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
    Draw(filePath)