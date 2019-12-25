import os

#Source Hex Plt Flie
file = open(r'Nintendo WiiU.txt', encoding='utf-8')
contents = file.read()

file2Write = None
try:
    file2Write = open(r'Nintendo WiiU.plt', 'w', encoding='utf-8')
except IOError:
    msg = 'Unable to create file on disk.'
    file2Write.close()
    print(msg)
finally:
    for content in contents.split():
        print(content)
        convent = int(content, 16)
        print(chr(convent))
        file2Write.write(chr(convent))
    file2Write.close()


