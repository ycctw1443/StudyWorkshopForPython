#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys

def main():
    args = sys.argv
    list1 = args[1].split(",")
    syain = int(list1[0])
    list1.pop(0)
    list2 = []
    i = 0
    while i < syain:
        list2 += list1[i].split("-")
        i += 1
    list3 = []
    i = 0
    while i < int(len(list1)):
        list3 += list1[i].split("-")
        i += 1
    from collections import Counter
    counted_dict = Counter(list3)
    from collections import OrderedDict
    a = OrderedDict(sorted(counted_dict.items(), key=lambda x:x[1], reverse=True))
    i = 0
    for item in a.keys():
        m = 0
        while m < int(len(list2)):
            if list2[m] == item:
                i = 1
                break
            else:
                m += 1
        if i == 1:
            print(item)
            print(a.get(item,))
            break



if __name__ == "__main__":
    main()
