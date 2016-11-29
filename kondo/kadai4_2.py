#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def main():
    args = sys.argv
    lenlist = args[1].split(",")
    str2 = lenlist[0].split("-")
    lenlist.pop(0)
    ribonlen = 0
    ribonnum = 0
    for index, item in enumerate(lenlist):
        if ribonlen > int(item):
            ribonlen = ribonlen - int(item)
        else:
            ribonlen = int(str2[1]) - int(item)
            ribonnum += 1
    print(ribonnum)
    
if __name__ =="__main__":
    main()

