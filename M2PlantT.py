#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
from tools.Utils import Generate

srcFileName = "mkList.txt"
outFileName = "mkList_temp.txt"

def M2PlantTree():
    readfp = open(srcFileName, "r", encoding='UTF-8') 
    writefp = open(outFileName, "w") 

    writefp.write("@startsalt\n{\n{T\n")

    while True:
        line = readfp.readline()
        if not line:
            break

        outLine = "++"
        for index in range(len(line)):
            if ' ' == line[index]:
                outLine += '+'

            if '*' == line[index]:
                break

        outLine += line[index + 1:]

        writefp.write(outLine)

    writefp.write("\n}\n}\n@endsalt\n")

    writefp.close()
    readfp.close()

    Generate(outFileName)

if __name__ == '__main__':
    M2PlantTree()