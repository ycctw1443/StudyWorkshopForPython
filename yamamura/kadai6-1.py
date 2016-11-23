#!/usr/bin/env python
# -*- coding:utf-8 -*-
import codecs


def main():
    datatxt = codecs.open("./data1.txt","r","utf-8")
    try:
        item = [x.strip() for x in datatxt]
    finally:
        datatxt.close()

    numribbon = item[0].split("-")
    num = int(numribbon[0])
    ribbon = int(numribbon[1])
    order = [int(y[0]) for y in item[1:]]

    i = 0
    used = 1
    while num > 0:
        if ribbon < order[i]:
            used += 1
            ribbon = int(numribbon[1])
        ribbon -= order[i]
        i += 1
        num -= 1
    print(used)

if __name__ == '__main__':
    main()

