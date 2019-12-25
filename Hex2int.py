import os
import sys

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

if __name__ == "__main__":
    ConventHex2IntPlt(sys.argv[1])
