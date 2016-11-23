#!/usr/bin/env python
# -*- coding:utf-8 -*-
import codecs
from collections import Counter


def main():
    datatxt = codecs.open("./data2.txt","r","utf-8")
    try:
        item = [x.strip() for x in datatxt]
    finally:
        datatxt.close()

    syain = int(item[0])
    syaindate = [e for es in item[1:syain+1] for e in es.split("-")]

    alldate = [e for es in item[1:] for e in es.split("-")]
    counted_dict = Counter(alldate)

    max_num = 0
    for date in sorted(syaindate):
        if date in counted_dict and counted_dict[date] > max_num:
            max_num = counted_dict[date]
            party_date = date
    print(party_date, max_num)


if __name__ == '__main__':
    main()

