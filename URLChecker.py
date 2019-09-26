import urllib.request
import time

import sys
print(sys.getdefaultencoding())


opener = urllib.request.build_opener() 
opener.addheaders = [('User-agent', 'Mozilla/49.0.2')] 
#这个是你放网址的文件名，改过来就可以了 
file = open(r'E:\Python Project\urllist.txt', encoding='utf-8') 
lines = file.readlines() 
url_list = [] 
for line in lines: 
  temp = line.replace('\n','')
  print(temp) 
  url_list.append(temp) 
#print(url_list) 
 
print('开始检查：') 
for url in url_list: 
  tempUrl = url 
  try : 
    opener.open(tempUrl) 
    print(tempUrl + '没问题') 
    #time.sleep(2) 
  except urllib.error.HTTPError: 
    print(tempUrl + '=访问页面出错') 
    time.sleep(2) 
  except urllib.error.URLError: 
    print(tempUrl + '=访问页面出错') 
    time.sleep(2) 
  time.sleep(0.1)