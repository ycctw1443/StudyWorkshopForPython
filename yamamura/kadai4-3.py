#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

def main():
    args = sys.argv
    input_str = args[1]
    item = [x.split("-") for x in input_str.split(",")]
    num = int(item[0][0])

    alldate = []
    [[alldate.append(e) for e in es] for es in item[1:]]
    from collections import Counter
    counted_dict = Counter(alldate)
    print(counted_dict)

    syaindate = []
    [[syaindate.append(b) for b in bs] for bs in item[1:num+1]]
    print(syaindate)

    max_num = 0  # 参加人数
    for date in sorted(syaindate):
        if date in counted_dict and counted_dict[date] > max_num:
            max_num = counted_dict[date]
            party_date = date
    print(party_date, max_num)

if __name__ == '__main__':
    main()
