#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from collections import Counter


def main():
    args = sys.argv
    input_str = args[1]
    item = [x.split("-") for x in input_str.split(",")]
    num = int(item[0][0])

    alldate = [e for es in item[1:] for e in es]
    counted_dict = Counter(alldate)

    syaindate = [e for es in item[1: num+1] for e in es]

    max_num = 0
    for date in sorted(syaindate):
        if date in counted_dict and counted_dict[date] > max_num:
            max_num = counted_dict[date]
            party_date = date
    print(party_date, max_num)

if __name__ == '__main__':
    main()

