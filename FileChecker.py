import os
DirPath = r'E:\Cutting Machine\FTP Sync\plt'

#plt、png、cdr文件所在目录列表
filedirpath_list = []
for i in os.walk(DirPath):
    for filename in i[2]:
        if (os.path.splitext(filename)[1] == '.plt') or (os.path.splitext(filename)[1] == '.png') or (os.path.splitext(filename)[1] == '.cdr'):
            #print("filename is: " + filename)
            #print("parent dir is: " + i[0])
            if i[0] not in filedirpath_list:
                filedirpath_list.append(i[0])
                        #filedirpath_list.append(os.path.join(i[0],filename))
                        



#查找plt、cdr、png文件缺失的型号
g_AllMissFileCount = 0
g_AllMoreThan3FileCount = 0
g_AllMoreThan3FilePath_list = []
g_AllHas3FilePath_list = []
for filedirpath in filedirpath_list:
    #print(filedirpath)
    Filecount = 0
    for i in os.listdir(filedirpath):
        #print(i)
        Filecount += 1

    #筛选目录下文件数目大于3个的文件目录
    if Filecount > 3:
        #print("文件夹中存在多余文件，请清理！！！：" + filedirpath)
        g_AllMoreThan3FileCount += 1
        g_AllMoreThan3FilePath_list.append(filedirpath)
        
        #print(i)
    #筛选目录下文件数目小于于3个的文件目录
    if Filecount < 3:
        g_AllMissFileCount += 1
        print("缺失文件型号：" + filedirpath)

    #筛选同时存在3个文件的目录
    if Filecount == 3:
        g_AllHas3FilePath_list.append(filedirpath)



#print("******************************************************************************")
print("总缺失文件型号个数 = %d"% g_AllMissFileCount)
print("******************************************************************************")

print("******************************************************************************")
print("同时存在3个文件的目录有%d个："% len(g_AllHas3FilePath_list))
print("******************************************************************************")


g_AllCDRPLTPNGFilePath = []
g_All3FlieButWrongPath = []
for fileHas3File in g_AllHas3FilePath_list:
    #print(fileHas3File)
    cdrpltpngCheck_Count = 0
    cdrpltpngCheck_String = ''
    for filename in os.listdir(fileHas3File):
        if cdrpltpngCheck_Count == 0:   #赋值为找到的第一个文件名
            cdrpltpngCheck_String = os.path.splitext(filename)[0]
        if (filename == cdrpltpngCheck_String + '.plt') or (filename == cdrpltpngCheck_String + '.png') or (filename == cdrpltpngCheck_String + '.cdr'):
            cdrpltpngCheck_Count += 1
    if cdrpltpngCheck_Count == 3:
        g_AllCDRPLTPNGFilePath.append(fileHas3File)
    else:
        g_All3FlieButWrongPath.append(fileHas3File)



print("******************************************************************************")
print("CDR PLT PNG文件同时存在且同名的文件目录有%d个："% len(g_AllCDRPLTPNGFilePath))
print("******************************************************************************")
# for cdrpltpngFile in g_AllCDRPLTPNGFilePath:
#     print("CDR PLT PNG文件同时存在的文件目录有：" + cdrpltpngFile)


print("******************************************************************************")
print("有三个文件但不同名或者格式错误的目录个数有%d个："% len(g_All3FlieButWrongPath))
for fliehas3ButWrongPath in g_All3FlieButWrongPath:
    print("有三个文件但不同名或者格式错误的目录有：" + fliehas3ButWrongPath)
print("******************************************************************************")


print("******************************************************************************")
print("总文件夹中存在多余文件个数 = %d"% len(g_AllMoreThan3FilePath_list))
for fileMoreThar3File in g_AllMoreThan3FilePath_list:
    print("文件夹中存在多余文件，请清理：" + fileMoreThar3File)
print("******************************************************************************")

#谨慎操作
#取消注释前确认是否是需要重命名
#查找文件中存在多个空格的文件并重命名
# for filedirpath in filedirpath_list:
#     #print(filedirpath)
#     for i in os.listdir(filedirpath):
#         while i.find('  ') != -1:
#             print("文件名中存在两个空格的文件有：" +i)
#             newFileName = i.replace('  ', ' ')
#             print("替换文件名中存在两个空格的文件有：" +newFileName)
#             os.rename(os.path.join(filedirpath, i), os.path.join(filedirpath, newFileName))
#             i = newFileName
