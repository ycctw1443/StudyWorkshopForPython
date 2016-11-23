#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def main():
    args = sys.argv
    input_str = args[1]
    item = [x.split("-") for x in input_str.split(",")]
    num = int(item[0][0])
    ribbon = int(item[0][1])
    order = [int(y[0]) for y in item[1:]]

    i = 0
    used = 1
    while num > 0:
        if ribbon < order[i]:
            used += 1
            ribbon = int(item[0][1])
        ribbon -= order[i]
        i += 1
        num -= 1
    print(used)

if __name__ == '__main__':
    main()

