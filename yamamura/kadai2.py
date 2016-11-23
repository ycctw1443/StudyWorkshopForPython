#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math


def main():
    print('半径を入力してください')
    r = float(input()) 
    ans = 2 * r * math.pi
    print('円周の長さは%f' % ans)


if __name__ == '__main__':
    main()
