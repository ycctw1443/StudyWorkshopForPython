#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def main():
    args = sys.argv
    list1 = args[1].split(",")
    syain = int(list1[0])
    list1.pop(0)
    list2 = list1[:syain-1:]
    list3 = list1[:len(list1)-1:]
    from collections import Counter,OrderedDict
    a = OrderedDict(sorted(Counter(list3).items(),
                    key=lambda x:x[1], reverse=True))
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
