#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import codecs


def main():
    args = []
    filedata = codecs.open("./data.txt","r","utf-8")
    try:
        for l in filedata:
            l = l.strip()
            args.append(l)
    finally:
        filedata.close()

    str1 = args[0].split("-")
    
    args.pop(0)
    ribonLen = 0
    ribonNum = 0
    for item in args:
        if ribonLen > int(item):
            ribonLen = ribonLen - int(item)
        else:
            ribonLen = int(str1[1]) - int(item)
            ribonNum += 1
    print(ribonNum)
    

if __name__ =="__main__":
    main()
