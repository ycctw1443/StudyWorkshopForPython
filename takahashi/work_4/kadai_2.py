#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import re

def main():
    inputData = sys.argv

    inputData = [int(data) for data in re.split(",|-",inputData[1])]
    ribonNum = 0
    ribonLen = inputData[1]
    now_len = 0
    print(inputData)

    for customer_len in inputData[2:]:
        if now_len < customer_len:
            ribonNum += 1
            now_len = ribonLen
        now_len -= customer_len
    
    print(ribonNum)

if __name__ == '__main__':
    main()
