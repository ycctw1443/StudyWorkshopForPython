#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import re
import codecs

def main():

    textData = codecs.open("./kadai_1_data.txt","r","utf-8")
    try:
        tmp = []
        for l in textData:
             l = l.strip()
             l = re.split(",|-",l)
             tmp.append(l)
    except:
        print("FILE_READ_ERROR")
    finally:
        textData.close()

    print(tmp)

    inputData = [i for i2 in tmp for i in i2]
    inputData = [int(data) for data in inputData]
    ribonNum = 0
    ribonLen = inputData[1]
    now_len = 0

    for customer_len in inputData[2:]:
        if now_len < customer_len:
            ribonNum += 1
            now_len = ribonLen
        now_len -= customer_len
   
    print(ribonNum)

if __name__ == '__main__':
    main()
