# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import sys
print(sys.getdefaultencoding())

#所有plt文件路径List
allPltFiles = []
#plt文件根目录
pltFileRootPath = "plt/"



def FindAllPltFilePath(path):
    g = os.walk(path) 
    for path, dir_list,file_list in g:  
        for file_name in file_list: 
            if os.path.splitext(file_name)[-1] == '.plt':
                print(os.path.join(path, file_name))
                allPltFiles.append(os.path.join(path, file_name))
    print("总共PLT文件为：%d"  %len(allPltFiles))
            

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
    return Coordinates_X, Coordinates_Y
   

def SaveCoordinatesJPG(coordsX, coordsY, filename):
    plt.xlabel('X', fontsize = 14)
    plt.ylabel('Y', fontsize = 14)

    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)

    # 设置每个坐标轴的取值范围
    plt.axis([0, 8000, 0, 6000]) 
    plt.legend(loc = 'best')    # 设置 图例所在的位置 使用推荐位置
    # 设置图表标题并给坐标轴加上标签
    plt.title(filename, fontsize = 24)
    plt.scatter(coordsY, coordsX, s = 3)
    plt.plot(coordsY, coordsX, color="r", linestyle="--", marker="*", linewidth=3.0)
    #plt.show() 
    #保存图象
    plt.savefig('ScreenProtectorJPG/' + filename + '.jpg')
    print("保存图片成功！！！") 
    plt.close()
    return


if __name__ == "__main__":
    FindAllPltFilePath(pltFileRootPath)
    i = 0
    for file in allPltFiles:
        tempPath = os.path.basename(file)
        fileName = os.path.splitext(tempPath)[0]
        (coordinateX, coordinateY) = CaculateCurrentPltCoordinates(file)
        SaveCoordinatesJPG(coordinateX, coordinateY, fileName)
        coordinateX.clear()
        coordinateY.clear()
        print("保存了%d个jpg！！！！！" %i)
        i += 1
    print("所有Plt绘制完成！！！！！")
