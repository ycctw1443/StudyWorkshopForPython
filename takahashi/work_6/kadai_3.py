#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
import collections
import codecs
import re

def main():

    textData = codecs.open("./kadai_3_data.csv","r","utf-8")
    try:
        tmp = []
        for l in textData:
             l = l.strip()
             l = re.split(",",l)
             tmp.append(l)
    except:
        print("FILE_READ_ERROR")
    finally:
        textData.close()   

    boxNum = int(len(tmp[0]))-1
    boxNameList = tmp[0][1::]
    boxList =  [[] for e in range(boxNum)]

    for item in tmp[1::]:
        for index,item2 in enumerate(item[1::]):
           boxList[index].append(item2)
            
    boxList =[[int(item) for item in box] for box in boxList] 
   
    printMostLuckyBox(boxList,boxNameList)
    printSecondPeopleLuckyProbability(boxList)
    mondai3(boxList,boxNum)

def printMostLuckyBox(boxList,boxNameList):
    probability = [ box[0] / sum(box) for box in boxList]
    maxIndex = probability.index(max(probability))

    print(boxNameList[maxIndex],int(round(probability[maxIndex]*100,0)) )

def printSecondPeopleLuckyProbability(boxList):
    firstSum = sum(item[0] for item in boxList)
    allSum = sum([item for item2 in boxList for item in item2])
    print(int(round(firstSum/allSum*100,0)))

def mondai3(boxList,boxNum):
    luckyNum = [item[0] for item in boxList]
    luckyProbab = [sum(box) for box in boxList]
    luckyProbab = [x/y for (x,y) in zip(luckyNum,luckyProbab)]
    luckyProbab =list(map(lambda x:1/boxNum*x,luckyProbab))
    luckyProbabOfA = luckyProbab[0]
    luckyProbab = sum(luckyProbab)

    print(int(round(luckyProbabOfA / luckyProbab * 100,0)))

if __name__ == '__main__':
    main()

    
