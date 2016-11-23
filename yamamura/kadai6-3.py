#!/usr/bin/env python
# -*- coding:utf-8 -*-
import codecs


def main():
    datacsv = codecs.open("./data.csv","r","utf-8")
    try:
        item = [x.strip() for x in datacsv]
    finally:
        datacsv.close()

    no1 = [int(x.strip()) for x in item[1][3:].split(",")]
    no2 = [int(x.strip()) for x in item[2][3:].split(",")]
    no3 = [int(x.strip()) for x in item[3][3:].split(",")]
   
    no1_box_a = no1[0] / (no1[0] + no2[0] + no3[0])
    no1_box_b = no1[1] / (no1[1] + no2[1] + no3[1])
    no1_box_c = no1[2] / (no1[2] + no2[2] + no3[2])

    max_kakuritu = 0
    for kakuritu in [no1_box_a, no1_box_b, no1_box_c]:
        if max_kakuritu < kakuritu:
            max_kakuritu = kakuritu
    if max_kakuritu == no1_box_a:
        box = "A"
    elif max_kakuritu == no1_box_b:
        box = "B"
    else:
        box = "C"
    print(box,max_kakuritu)

    zirou_no1 = (no1_box_a + no1_box_b + no1_box_c) / 3
    print(zirou_no1)

    no1_sum = sum(no1)
    no2_sum = sum(no2)
    no3_sum = sum(no3)
    all_sum = no1_sum + no2_sum + no3_sum
    box_a_kakuritu = (no1[0] + no2[0] + no3[0]) / all_sum
    zirou_no1_boxa = ((1/3) * no1_box_a) / zirou_no1

    print(zirou_no1_boxa)


if __name__ == '__main__':
    main()

