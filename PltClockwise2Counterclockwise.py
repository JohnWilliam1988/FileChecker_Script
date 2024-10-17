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

allCounterclockwiseCoordinates = []

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
    pointX_All = []
    pointY_All = []

    bClockwise = True
    currentPathPointX_All = []
    for coordinate in contents.split():
        print(coordinate)
        if (coordinate[0] == 'U'):
            coordinate = coordinate.strip('U')
            coordinate = coordinate.split(',', 1)
            pointX.append(int(coordinate[0]))
            print("len(currentPathPointX_All) is %d " % (len(currentPathPointX_All)))
            if len(currentPathPointX_All) > 1:
                maxPathX = max(currentPathPointX_All)
                minPathX = min(currentPathPointX_All)
                maxIndex = currentPathPointX_All.index(maxPathX)
                minIndex = currentPathPointX_All.index(minPathX)
                bClockwise = maxIndex < minIndex
                print("顺时针 maxIndex %d, minIndex %d" % (maxIndex, minIndex))
            currentPathPointX_All.clear()
            currentPathPointX_All.append(int(coordinate[0]))
            pointX_All.append(int(coordinate[0]))
            pointY.append(int(coordinate[1]))
            pointY_All.append(int(coordinate[1]))
            bDown = False
        elif (coordinate[0] == 'D'):
            coordinate = coordinate.strip('D')
            coordinate = coordinate.split(',', 1)
            pointX.append(int(coordinate[0]))
            currentPathPointX_All.append(int(coordinate[0]))
            pointX_All.append(int(coordinate[0]))
            pointY.append(int(coordinate[1]))
            pointY_All.append(int(coordinate[1]))
            bDown = True
        else:
            continue


        #有两个点才能进行绘制
        if len(pointX) > 1 :       
            #绘制提刀运动轨迹
            if bDown :
                plt.plot(pointX, pointY, color = "r", linewidth = 1)
            #绘制切割运动轨迹
            else:
                plt.plot(pointX, pointY, linestyle = 'dotted', color = "b", linewidth = 1)

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

    #开始写入,计算图案的中心点
    maxX = max(pointX_All)
    minX = min(pointX_All)
    midX = (maxX - minX) / 2

    allMirrorPt = []
    for coordinate in contents.split():
        if (coordinate[0] == 'U'):
            coordinate = coordinate.strip('U')
            coordinate = coordinate.split(',', 1)
            if int(coordinate[0]) < midX :
                mirrorPtX = int(coordinate[0]) + 2 * (midX - int(coordinate[0]))
            elif int(coordinate[0]) > midX :
                mirrorPtX =  int(coordinate[0]) - 2 * (int(coordinate[0]) - midX)
            else :
                mirrorPtX = midX
            
            allMirrorPt.append('U%d,%d ' % (mirrorPtX, int(coordinate[1]) ))
            
        elif (coordinate[0] == 'D'):
            coordinate = coordinate.strip('D')
            coordinate = coordinate.split(',', 1)
            if int(coordinate[0]) < midX :
                mirrorPtX = int(coordinate[0]) + 2 * (midX - int(coordinate[0]))
            elif int(coordinate[0]) > midX :
                mirrorPtX =  int(coordinate[0]) - 2 * (int(coordinate[0]) - midX)
            else :
                mirrorPtX = midX
            
            allMirrorPt.append('D%d,%d ' % (mirrorPtX, int(coordinate[1]) ))

        else:
            continue

    for miPt in allMirrorPt:
        print(miPt)

def get_points(filePath) :
    #Mac格式
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    tempPath = os.path.basename(filePath)
    fileName = os.path.splitext(tempPath)[0]
    contents = file.read()

    allpoints = []
    for coordinate in contents.split():
        print(coordinate)
        if (coordinate[0] == 'U'):      
            if len(allpoints) > 0:
                print(allpoints)
                check_clockwise_triplets(allpoints)
                allpoints.clear()
            coordinate = coordinate.strip('U')
            coordinate = coordinate.split(',', 1)
            curpt = [int(coordinate[0]), int(coordinate[1])]
            allpoints.append(curpt)
        elif (coordinate[0] == 'D'):      
            coordinate = coordinate.strip('D')
            coordinate = coordinate.split(',', 1)
            curpt = [int(coordinate[0]), int(coordinate[1])]
            allpoints.append(curpt)
        else:
            continue

    
def check_clockwise_triplets(points):
    n = len(points)
    if n < 3:
        return None  # 至少需要3个点来形成多边形

    #连续的顺时针方向计数
    clockwise_index = 0 
    #最大连续的顺时针方向计数
    max_clockwise_index = 0
    #连续的逆时针方向计数
    counter_clockwise_index = 0
    #最大连续的逆时针方向计数
    max_counter_clockwise_index = 0

  
    for i in range(n):
        triplet = points[i:i+3]  # 获取当前点及其后面的两个点
        if len(triplet) < 3:
            break  # 不足三个点，退出循环

        x1, y1 = triplet[0]
        x2, y2 = triplet[1]
        x3, y3 = triplet[2]

        # 计算叉积
        cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

        if cross_product > 0:
            # print("逆时针")
            counter_clockwise_index += 1
            #出现逆时针，清零顺时针计数
            if clockwise_index > 0 :
                clockwise_index = 0
            if max_counter_clockwise_index < counter_clockwise_index :
                max_counter_clockwise_index = counter_clockwise_index
        elif cross_product < 0:
            # print("顺时针")
            clockwise_index += 1
            #出现顺时针，清零连续逆时针计数
            if counter_clockwise_index > 0 :
                counter_clockwise_index = 0
            if max_clockwise_index < clockwise_index :
                max_clockwise_index = clockwise_index
        else:
            # print("共线")
            clockwise_index = 0
            counter_clockwise_index = 0

    print("顺时针最大连续次数:%d 逆时针最大连续次数:%d" % (max_clockwise_index, max_counter_clockwise_index))

    #计算当前path中心点
    x_coordinates = [point[0] for point in points]
    y_coordinates = [point[1] for point in points]
    x_min = min(x_coordinates)
    print("x_min %d " % (x_min))
    y_min = min(y_coordinates)
    print("y_min %d " % (y_min))
    x_max = max(x_coordinates)
    print("x_max %d " % (x_max))
    y_max = max(y_coordinates)

    #如果不是逆时针
    if max_clockwise_index >= max_counter_clockwise_index:   
       for i, pt in enumerate(x_coordinates):
            
            if i == len(x_coordinates) - 1 :
                pt = 'U%d,%d ' % (x_coordinates[i], y_coordinates[i])
            else :
                pt = 'D%d,%d ' % (x_coordinates[i], y_coordinates[i])
            
            allCounterclockwiseCoordinates.insert(0, pt)
    else:
        for i, pt in enumerate(x_coordinates):
            if i == 0 :
                pt = 'U%d,%d ' % (x_coordinates[i], y_coordinates[i])
            else :
                pt = 'D%d,%d ' % (x_coordinates[i], y_coordinates[i])

            allCounterclockwiseCoordinates.append(pt)

    # DrawPoints(points, max_clockwise_index >= max_counter_clockwise_index)

def DrawPoints(coordinates, clockwise): 
    plt.figure(num = 1, figsize = (15, 15), dpi = 100)
    ax = plt.gca()
    #x轴方向调整：
    ax.xaxis.set_ticks_position('top') #将x轴的位置设置在顶部
    ax.invert_xaxis() #x轴反向
    
    #y轴方向调整：
    ax.yaxis.set_ticks_position('right') #将y轴的位置设置在右边
    ax.invert_yaxis() #y轴反向

    x_coordinates = [point[0] for point in coordinates]
    y_coordinates = [point[1] for point in coordinates]
    if clockwise :
        plt.plot(x_coordinates, y_coordinates, color = "r", linewidth = 1)
    else :
        plt.plot(x_coordinates, y_coordinates, color = "g", linewidth = 1)


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
    # filePath = '/Users/zhoujunliang/Downloads/aaa.plt'
    # DrawPlt2(filePath)
    # 获取入口参数个数
    num_arguments = len(sys.argv)
    print("传参个数为 %d" % (num_arguments))
    if num_arguments != 3:
        print("******参数错误******\n参数一:源Plt文件路径\n参数二:逆时针Plt文件路径")
    else:
        sourceFilePath = sys.argv[1]
        mirroredFilePath = sys.argv[2]
        get_points(sourceFilePath)
        # print("all mirrored pt is ")
        # 使用 "with" 语句来自动管理文件的打开和关闭
        with open(mirroredFilePath, "w") as file:
            file.write("IN IN ")
            for pt in allCounterclockwiseCoordinates :
                print(pt)
                file.write(pt)
            file.write("U0,0 @ ")
        print("SUCESS\n逆时针Plt文件已创建并写入完成!")
        
        
    

   
