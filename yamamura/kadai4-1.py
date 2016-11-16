#!/usr/bin/env python
# -*- coding:utf-8 -*-

fruits =["apple", "orange", "lemon", "strawberry", "apple", "cherry", "melon", "apple", "lemon"]

def main():
    fruits.reverse()
    value1 = [x for x in fruits]
    print(value1)

    fruits.reverse()
    value2 = [y[::-1] for y in fruits]
    print(value2)

    fruits.reverse()
    from collections import Counter
    counted_dict = Counter(fruits)
    print(counted_dict)

    value3 = {item: len(item) for item in fruits}
    print(value3)

    value4 = {z: len(z) for z in fruits}
    value4 = sorted(value4, key=lambda x:x[1],  reverse=True)
    print(value4)


if __name__ == '__main__':
    main()
