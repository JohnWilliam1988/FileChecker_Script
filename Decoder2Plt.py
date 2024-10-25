import os
import sys
import re

import DrawPltVer2

def writefile(filepath, contents):
    rootdir = os.path.dirname(filepath)
    filename = os.path.splitext(filepath)[0]
    decoderfilepath = os.path.join(rootdir, filename + ".plt")
    # print("decoderfilepath ", decoderfilepath)
    with open(decoderfilepath, 'w') as file:
        # 将字符串写入文件
        for content in contents:
            file.write(content + " ")
        file.close()
        print("Plt转换完成")
        DrawPltVer2.Draw(decoderfilepath)

def decoder(password, contents):
    P = []
    P.append(password[1])
    P.append(password[3])
    P.append(password[5])
    P.append(password[7])
    P.append(password[9])
    P.append(password[0])
    P.append(password[2])
    P.append(password[4])
    P.append(password[6])
    P.append(password[8])

    recoveredPltString = []
    allContents = contents.split( )   # 以空格为分隔符，包含 \n
    # print(len(allContents));    
    for content in allContents:
        if (content[0] == "D") or (content[0] == "U"):
            pt = ""
            for s in content:
              positions = [index for index, value in enumerate(P) if value == s]
            #   print("positions is ", positions)
              if len(positions) > 0:
                  pt += str(positions[0])
              else:
                  pt += s
            recoveredPltString.append(pt)
        elif "WSJP=" in content:
            #WSJP=解密后原始密码不需要了
            continue
        else:
            recoveredPltString.append(content)

    return recoveredPltString



# #将密码复位
def fixpassword(password):
    unusedNumber = []
    for i in range(10):
        if str(i) in password:
            continue
        else:
            unusedNumber.append(str(i))
    print(unusedNumber)

    index = 0
    fixedPassword = ""
    for i, p in enumerate(password):
        if (p == 'X'):
            fixedPassword += unusedNumber[index]
            index += 1
        else:
            fixedPassword += p
        
    print(fixedPassword)
    return fixedPassword

# 重复出现的数字用X替换
def replace_greater_than_second_duplicate_with_x(wsjp_number):
    replacedX = ""
    for i in wsjp_number:
        if (len(replacedX) == 0):
            replacedX += i
        else:
            if i in replacedX:
                replacedX += "X"
            else:
                replacedX += i

    return replacedX
    
#截取原始密码
def getpassword(content):
    # 编写正则表达式
    pattern = r'WSJP=(\d{10})'
    # 使用正则表达式进行匹配
    match = re.search(pattern, content)

    # 提取匹配到的结果
    if match:
        wsjp_number = match.group(1)
        print("匹配到的数字为:", wsjp_number)
        result = replace_greater_than_second_duplicate_with_x(wsjp_number)
        print(result)
        password = fixpassword(result)
        return password
       
    else:
        print("未匹配到数字")
        return 0;

#读取加密文件
def parserfile(source):
    file = open(filePath, encoding='utf-8')
    print("文件路径为： " + file.name)
    tempPath = os.path.basename(filePath)
    print("tempPath is ", tempPath)
    contents = file.read()
    print(contents)
    return contents
    

if __name__ == "__main__":
    filePath = "/Users/zhoujunliang/Desktop/200714185004-136.sjc"
    contents = parserfile(filePath)
    psd = getpassword(contents)
    if psd != 0:
        recovedsjc = decoder(psd, contents)
        writefile(filePath, recovedsjc)

    # argumentslen = len(sys.argv)
    # print("传参个数为 %d" % (argumentslen))
    # if argumentslen == 2 :
    #     # filePath = "/Users/zhoujunliang/Downloads/Data/待破解文件/211201165905-32892.sjc"
    #     filePath = sys.argv[1]
    #     contents = parserfile(filePath)
    #     psd = getpassword(contents)
    #     if psd != 0:
    #         recovedsjc = decoder(psd, contents)
    #         writefile(filePath, recovedsjc)
    # else:
    #     print("请输入sjc源文件路径")
    
   