#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import codecs


def main():
    args = []
    fin = codecs.open("./data1.txt","r","utf-8")
    try:
        for l in fin:
            l = l.strip()
            args.append(l)
    finally:
        fin.close()

    syain = int(args[0])
    args.pop(0)
    bite = int(len(args)) - syain
    list2 = []
    i = 0
    while i < syain:
        list2 += args[i].split("-")
        i += 1
    list3 = []
    i = 0
    args.reverse()
    while i < bite:
        list3 += args[i].split("-")
        i += 1
    
    okDay = []
    for item in list3:
        if item not in list2:
            list3.remove(item)
        
    okDay = list2 + list3
    from collections import Counter
    counted_dict = Counter(okDay)
    okMax = max(counted_dict.values())
    okDay=[]
    for k,v in counted_dict.items():
        if v == okMax:
            okDay.append(k) 
    okDay.sort()
    print("開催日：",okDay[0])
    print("参加人数",okMax)
if __name__ == "__main__":
    main()
