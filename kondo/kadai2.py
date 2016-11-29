#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

def main():
    print("半径を入力してください")
    name = float(input())
    name = name * 2 * math.pi
    print("円周の長さは%fです" % name)

if __name__ =="__main__":
    main()
