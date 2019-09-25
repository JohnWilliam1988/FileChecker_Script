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
for filedirpath in filedirpath_list:
    #print(filedirpath)
    Filecount = 0
    for i in os.listdir(filedirpath):
        Filecount += 1

    if Filecount > 3:
        #print("文件夹中存在多余文件，请清理！！！：" + filedirpath)
        g_AllMoreThan3FileCount += 1
        g_AllMoreThan3FilePath_list.append(filedirpath)
        
        #print(i)
    if Filecount < 3:
        g_AllMissFileCount += 1
        print("缺失文件型号：" + filedirpath)

print("**************************")
print("总缺失文件型号个数 = %d"% g_AllMissFileCount)
print("**************************")


for fileMoreThar3File in g_AllMoreThan3FilePath_list:
    print("文件夹中存在多余文件，请清理：" + fileMoreThar3File)

print("**************************")
print("总文件夹中存在多余文件个数 = %d"% len(g_AllMoreThan3FilePath_list))
print("**************************")

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
