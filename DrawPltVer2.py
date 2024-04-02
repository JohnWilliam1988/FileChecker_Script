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


def DrawPlt2(filePath):
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

def relative_to_absolute_path(path):
    # 将SVG路径中的相对坐标转换为绝对坐标
    commands = ['M', 'L', 'H', 'V', 'C', 'S', 'Q', 'T', 'A']
    values_per_command = {'M': 2, 'L': 2, 'H': 1, 'V': 1, 'C': 6, 'S': 4, 'Q': 4, 'T': 2, 'A': 7}
    current_pos = [0, 0]
    abs_path = []
    for i, token in enumerate(path):
        if token in commands:
            # 处理路径命令
            values = path[i+1:i+1+values_per_command[token]]
            if token == 'M':
                # M命令的第一个点为绝对坐标
                current_pos = values[:2]
                abs_path.append(['M'] + current_pos)
                values = values[2:]
                token = 'L'
            elif token == 'm':
                # m命令的第一个点为相对坐标
                current_pos[0] += values[0]
                current_pos[1] += values[1]
                abs_path.append(['M'] + current_pos)
                values = values[2:]
                token = 'l'
            for j in range(0, len(values), 2):
                # 将相对坐标转换为绝对坐标
                if token in ('l', 't'):
                    values[j] += current_pos[0]
                    values[j+1] += current_pos[1]
                elif token in ('h',):
                    values[j] += current_pos[0]
                elif token in ('v',):
                    values[j] += current_pos[1]
                elif token in ('c',):
                    values[j] += current_pos[0]
                    values[j+1] += current_pos[1]
                    values[j+2] += current_pos[0]
                    values[j+3] += current_pos[1]
                    values[j+4] += current_pos[0]
                    values[j+5] += current_pos[1]
                elif token in ('s', 'q'):
                    values[j] += current_pos[0]
                    values[j+1] += current_pos[1]
                    values[j+2] += current_pos[0]
                    values[j+3] += current_pos[1]
                elif token in ('a',):
                    values[j+5] += current_pos[0]
                    values[j+6] += current_pos[1]
                current_pos = values[j:j+2]
            abs_path.append([token] + values)
    return abs_path


if __name__ == "__main__":
    filePath = '/Users/zhoujunliang/Downloads/aaa.plt'
    DrawPlt2(filePath)
    # path = 'M 8.98 8.8 L 74.98 8.8 L 74.98 75.8 L 8.98 75.8 z'
    # abspath = relative_to_absolute_path(path)
    # print(len(abspath))
    # for i in abspath:
    #     print("pt is ", i)