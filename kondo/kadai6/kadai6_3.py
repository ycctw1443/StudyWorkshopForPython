#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import codecs


def main():
    args = []
    filedata = codecs.open("./data3.csv","r","utf-8")
    try:
        for l in filedata:
            l = l.strip()
            args.append(l)
    finally:
        filedata.close()
    boxname = args.pop(0).split(",")
    boxname.pop(0)
    gradeint = len(args)
    detail = []
    for item in args:
        list1 = item.split(",")
        list1.pop(0)
        detail += list1

    boxa = makeBox(0,detail,gradeint)
    boxb = makeBox(1,detail,gradeint)
    boxc = makeBox(2,detail,gradeint)

    parselist = [prize(boxa),prize(boxb),prize(boxc)]

    prizedic =dict(zip(boxname,parselist))
    
    ichirobox = ""
    for k, v in prizedic.items():
        if v == max(prizedic.values()):
            ichirobox = k
    print("問題１",ichirobox,round(100*max(prizedic.values())))
    print("問題２",round(100*(1/gradeint)*(sum(prizedic.values()))))
    print("問題３",round(100*(parselist[0]/sum(prizedic.values()))))

def makeBox(boxnum,detail,gradeint):
    box = []
    while boxnum < int(len(detail)):
        box.append(detail[boxnum])
        boxnum += gradeint
    return box

def prize(detail):
    allnum = 0
    for item in detail:
        allnum += int(item)
    parse = int(detail[0]) / allnum 
    return parse

if __name__ =="__main__":
    main()
