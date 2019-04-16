#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess

def Generate(fileName):

    cmd = "java -jar plantuml.jar " + fileName
    process = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output

if __name__ == '__main__':
    pass