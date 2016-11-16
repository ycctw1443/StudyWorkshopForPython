#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

def main():
    args =sys.argv
    str1 = args[1].split(",")
    str2 = str1[0].split("-")
    str1.pop(0)
    ribonLen = 0
    ribonNum = 0
    for index, item in enumerate(str1):
        if ribonLen > int(item):
            ribonLen = ribonLen - int(item)
        else:
            ribonLen = int(str2[1]) - int(item)
            ribonNum += 1
    print(ribonNum)
    

if __name__ =="__main__":
    main()
