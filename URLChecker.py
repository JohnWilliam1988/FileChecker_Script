import urllib.request
import urllib.parse
import codecs
import string
import time

import sys
print(sys.getdefaultencoding())

file = open(r'E:\Cutting Machine\Project\FileChecker_Script\disableurllist.txt', encoding='utf-8') 
lines = file.readlines() 
url_list = [] 
for line in lines: 
  temp = line.replace('\n','')
  print(temp) 
  url_list.append(temp) 
#print(url_list) 

print('********************************************************************************************')
print('URL总数为：%d'%len(url_list))
print('********************************************************************************************')


print('********************************************************************************************') 
print('开始检查：') 

opener = urllib.request.build_opener() 
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')] 
#这个是你放网址的文件名，改过来就可以了 
avaliable_count = 0
failedUrlList = []
file = codecs.open(r'E:\Cutting Machine\Project\FileChecker_Script\unusefulurllist.txt', 'w', 'utf-8')
for url in url_list: 
  tempUrl = url 
  try : 
     #处理包含中文路径的URL
    opener.open(urllib.parse.quote(tempUrl, safe=string.printable))
    print(tempUrl + '  PASS！！！') 
    avaliable_count += 1
    #time.sleep(2) 
  except urllib.error.HTTPError: 
    print(tempUrl + ' FAILED！！！！！！！！') 
    failedUrlList.append(tempUrl)
    file.write(tempUrl)
    file.write('\n')
    time.sleep(2) 
  except urllib.error.URLError: 
    print(tempUrl + ' FAILED！！！！！！！！') 
    failedUrlList.append(tempUrl)
    file.write(tempUrl)
    file.write('\n')
    time.sleep(2) 
  time.sleep(0.05)


file.close()

print('********************************************************************************************') 
print('********************************************************************************************') 
print('检查URL总数为：%d'%len(url_list))
print('有效URL总数：%d' % avaliable_count)
print('失效URL总数：%d'% len(failedUrlList))

for url in failedUrlList:
  print('失效URL: '+url)
print('********************************************************************************************') 