#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def Generate(fileName, fileType):

    if fileType == "png":
        cmd = "java -jar plantuml.jar " + fileName
    else:
        cmd = "java -jar plantuml.jar -tsvg " + fileName

    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output

if __name__ == '__main__':
    pass