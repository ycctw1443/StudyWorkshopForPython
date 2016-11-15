#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys


def main():
    inputData = sys.argv


    a = inputData[1].split(",")
    b = a[0].split("-")
    for index, item in enumerate(a):
        if index != 0:
            b.append(a[index])


    ribonNum = 1
    ribonLen = int(b[1])
   
    for i in range(int(b[0])):
        if(ribonLen < int(b[i+2])):
            ribonNum += 1
            ribonLen = int(b[1])
        ribonLen -= int(b[i+2])
    
    print(ribonNum)

if __name__ == '__main__':
    main()
