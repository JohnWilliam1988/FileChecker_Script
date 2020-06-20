# -*- coding: utf-8 -*-
import os
import platform
import sys
import requests
import matplotlib.pyplot as plt
from PIL import Image
import xlrd
import time
print(sys.getdefaultencoding())

#Tip 家里电脑中文编码乱码
#plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
#修改为以下后正常
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['font.family']='sans-serif'
#修改中文负号乱码
plt.rcParams['axes.unicode_minus'] = False 


SYSSTRING = platform.system()

#所有plt文件路径List
allPltFiles = []

#plt文件根目录
pltFileRootPath = ''
#plt文件坐标图保存路径
pltSavedJPGPath = ''

def sysInit():
    global pltFileRootPath
    global pltSavedJPGPath
    if(SYSSTRING == "Windows"):
        print ("Call Windows tasks")
        pltFileRootPath = '纵向\\'
        pltSavedJPGPath = '线框图\\'
    elif(SYSSTRING == "Linux"):
        print ("Call Linux tasks")
    elif(SYSSTRING == "Darwin"):
        print ("Call Darwin tasks")
        pltFileRootPath = "plt/"
        pltSavedJPGPath = "pltJPG1/"
    else:
        print ("Other System tasks")

    
    

    return

            

def CaculateCurrentPltCoordinatesAndDraw(filePath):
    #存储当前Plt文件坐标List
    Coordinates_X = []
    Coordinates_Y = []
    coordsX = []
    coordsY = []
    #Mac格式
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    tempPath = os.path.basename(filePath)
    fileName = os.path.splitext(tempPath)[0]
    contents = file.read()

    plt.figure(num = 1, figsize = (15, 15), dpi = 100)
    ax = plt.gca()

    #x轴方向调整：
    ax.xaxis.set_ticks_position('top') #将x轴的位置设置在顶部
    ax.invert_xaxis() #x轴反向

    #y轴方向调整：
    ax.yaxis.set_ticks_position('right') #将y轴的位置设置在右边
    ax.invert_yaxis() #y轴反向

    # 设置刻度标记的大小
    #plt.tick_params(axis='both', which='major', labelsize = 14)

    # 设置每个坐标轴的取值范围
    #plt.axis([0, 8000, 0, 6000]) 
    
    # 设置图表标题并给坐标轴加上标签
    #plt.title(fileName, fontsize = 18)

    #print(contents)
    for coordinate in contents.split():
        #print(coordinate)
        if (coordinate[0] == 'U'):
            if ((len(coordsX) > 0) and (len(coordsY) > 0 )):
                plt.plot(coordsX, coordsY, color = "black", linestyle = 'solid', linewidth = 4)

            coordsX.clear()
            coordsY.clear()
            continue
        if (coordinate[0] == 'D'):
            coordinate = coordinate.strip('D')
            #print(coordinate)
            coordinate = coordinate.split(',', 1)
            #print(coordinate[0])
            #print(coordinate[1])
            Coordinates_X.append(int(coordinate[0]))
            coordsX.append(int(coordinate[0]))
            Coordinates_Y.append(int(coordinate[1]))
            coordsY.append(int(coordinate[1]))
            #continue
        
            

    # width = (max(Coordinates_X) - min(Coordinates_X)) / 40
    # height = (max(Coordinates_Y) - min(Coordinates_Y)) / 40

    # font = {'family': 'sans-serif',
    #     'color':  'blue',
    #     'weight': 'normal',
    #     'size': 16,
    #     }

    # xLableTitle = "宽：" + str(width) + " mm"
    # yLableTitle = "高：" + str(height) + " mm"

    # plt.xlabel(xLableTitle, font)
    # plt.ylabel(yLableTitle, font)

    
    #设置 图例所在的位置 使用推荐位置
    #plt.legend(loc = 'best') 

    plt.axis("equal")
    plt.axis('off')
    
    # toggle fullscreen mode
    #plt.get_current_fig_manager().full_screen_toggle() 
    # plt.show() 
    # print("Show Completed！！！")

    #保存图象
    #加入同名文件存在处理，还可以改进，要判断到确认没有同名文件为止
    savePngPath = pltSavedJPGPath + fileName + '.png'
    if os.path.exists(savePngPath):
        print(savePngPath + ' File Already Exist!!!!!!')
        plt.savefig(pltSavedJPGPath + fileName + 'exist.png', transparent=True)
        # #read the image
        # im = Image.open(pltSavedJPGPath + fileName + 'exist.png')
        # #rotate image by 180 degrees
        # angle = 180
        # out = im.rotate(angle, expand = True)
        # out.save(pltSavedJPGPath + fileName + 'exist.png')
        print("保存图片成功！！！") 
    else:
        plt.savefig(savePngPath, transparent=True)
        # #read the image
        # im = Image.open(savePngPath)
        # #rotate image by 180 degrees
        # angle = 180
        # out = im.rotate(angle, expand = True)
        # out.save(savePngPath)
        print("保存图片成功！！！") 
    plt.close()

    return
   

def DownloadPltfile(pltUrl):
    plt_url = pltUrl
    fileName = os.path.basename(plt_url)
    r = requests.get(plt_url) 
    with open("D://DownloadPlt//" + fileName,'wb') as f:
        f.write(r.content)
        print("Download Plt file completed!!!")
        time.sleep(0.01)
        return "D://DownloadPlt//" + fileName


def excel_data(file= "E:\Python Project\FileChecker_Script\AllPltsUrl.xlsx"):
    try:
        # 打开Excel文件读取数据
        data = xlrd.open_workbook(file)
        # 获取第一个工作表2
        table = data.sheet_by_index(0)
        # 获取行数
        nrows = table.nrows
        # 获取列数
        ncols = table.ncols

        print("行数:%d\n", nrows)
        print("列数:%d\n", ncols)

        pltUrlList = []

        for row in range(0, nrows):
            pltUrl = table.cell(row, 0).value
            print(pltUrl + " %d ", row)
            pltUrlList.append(pltUrl)
        
        return pltUrlList

    except Exception as e:
         print ('Exception: ', e)

    


if __name__ == "__main__":
    ##批量遍历Plt文件
    # sysInit()
    # FindAllPltFilePath(pltFileRootPath)
    # i = 0
    # for file in allPltFiles:
    #     tempPath = os.path.basename(file)
    #     fileName = os.path.splitext(tempPath)[0]
    #     (coordinateX, coordinateY) = CaculateCurrentPltCoordinates(file)
    #     SaveCoordinatesJPG(coordinateX, coordinateY, fileName)
    #     #coordinateX.clear()
    #     #coordinateY.clear()
    #     print("保存了%d个jpg！！！！！" %i)
    #     i += 1
    # print("所有Plt绘制完成！！！！！")

    #显示单个Plt文件
    sysInit()
    urlList = excel_data()
    #fileUrl = sys.argv[1]
    for url in urlList:
        fileUrl = url
        filePath = DownloadPltfile(fileUrl)
        tempPath = os.path.basename(filePath)
        #fileName = os.path.splitext(tempPath)[0]
        CaculateCurrentPltCoordinatesAndDraw(filePath)
        #DrawPlt(coordinateX, coordinateY, fileName)
