# -*- coding: utf-8 -*-
import os
import platform
import sys
import matplotlib.pyplot as plt
import numpy as np
print(sys.getdefaultencoding())
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


SYSSTRING = platform.system()

def ConventHex2IntPlt(file_Path):
    #Source Hex Plt Flie
    Sourcefile = open(file_Path, encoding='utf-8')
    contents = Sourcefile.read()
    (filepath, tempfilename) = os.path.split(file_Path)
    (filename, extension) = os.path.splitext(tempfilename)
    print('filepath is : ' + filepath)
    print('filename is : ' + filename)
    print('extension is : ' + extension)

    writeFilePath = os.path.join(filepath, filename + '.plt')
    print('writeFilePath is :' + writeFilePath)
    file2Write = None
    try:
        file2Write = open(writeFilePath, 'w', encoding='utf-8')
    except IOError:
        msg = 'Unable to create file on disk.'
        file2Write.close()
        print(msg)
    finally:
        for content in contents.split():
            #print(content)
            convent = int(content, 16)
            #print(chr(convent))
            file2Write.write(chr(convent))
        file2Write.close()
        print('Convent Done!!!')
    return

def CaculateCurrentPltCoordinates(filePath):
    #存储当前Plt文件坐标List
    Coordinates_X = []
    Coordinates_Y = []
    #Mac格式
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    # tempPath = os.path.basename(filePath)
    # fileName = os.path.splitext(tempPath)[0]
    contents = file.read()
    #print(contents)
    for coordinate in contents.split():
        #print(coordinate)
        if (coordinate[0] == 'D'):
            coordinate = coordinate.strip('D')
            #print(coordinate)
            coordinate = coordinate.split(',', 1)
            #print(coordinate[0])
            #print(coordinate[1])
            Coordinates_X.append(int(coordinate[0]))
            Coordinates_Y.append(int(coordinate[1]))
    return Coordinates_X, Coordinates_Y


def ShowPlt(file1Path, file2Path):
    #开启一个窗口，num设置子图数量，这里如果在add_subplot里写了子图数量，num设置多少就没影响了
    #figsize设置窗口大小，dpi设置分辨率
    fig = plt.figure(num = 1, figsize = (15, 8),dpi = 100)
    # 设置图表标题并给坐标轴加上标签
    #plt.title('PLT文件对比', fontsize = 24)
    #使用add_subplot在窗口加子图，其本质就是添加坐标系
    #三个参数分别为：行数，列数，本子图是所有子图中的第几个，最后一个参数设置错了子图可能发生重叠
    #ax1 = fig.add_subplot(1,1,1)  
    #ax2 = fig.add_subplot(2,1,2)
    (coordinateY, coordinateX) = CaculateCurrentPltCoordinates(file1Path)
    tempPath = os.path.basename(file1Path)
    fileName = os.path.splitext(tempPath)[0]
    #绘制曲线 
    plt.plot(coordinateX, coordinateY, color='g', label = fileName)
     # 设置 图例所在的位置 使用推荐位置
    plt.legend(loc = 'best')
    (coordinateY, coordinateX) = CaculateCurrentPltCoordinates(file2Path)
    tempPath = os.path.basename(file2Path)
    fileName = os.path.splitext(tempPath)[0]
    plt.plot(coordinateX, coordinateY, color='r', label = fileName)
     # 设置 图例所在的位置 使用推荐位置
    plt.legend(loc = 'best')
    #ax1.plot(np.arange(0,1,0.1),range(0,10,1),color='g')
    #同理，在同一个坐标系ax1上绘图，可以在ax1坐标系上画两条曲线，实现跟上一段代码一样的效果
    #ax1.plot(np.arange(0,1,0.1),range(0,20,2),color='b')
    #在第二个子图上画图
    #ax2.plot(np.arange(0,1,0.1),range(0,20,2),color='r')
    plt.show()


if __name__ == "__main__":
    #file1 = '红米 Note 8 (缅甸定制)_Hex 12.31.plt'
    #file2 = 'xiaomi 8.plt'
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    ShowPlt(file1, file2)
   
