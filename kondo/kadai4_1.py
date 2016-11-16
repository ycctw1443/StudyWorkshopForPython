#!/usr/bin/env python
#-*- coding:utf-8 -*-

def main():
    fruits = ["apple","orange","lemon","strawberry","apple","cherry","melon","apple","lemon"]
    print(fruits[::-1])
    print([item[::-1] for item in fruits])
    from collections import Counter
    counted_dict = Counter(fruits)
    print(counted_dict)
    dic = {}
    for item in fruits:
        num = len(item)
        dic.update({item:num})
    print(dic)
    for key,value in sorted(dic.items(),key=lambda x:x[1],reverse=True):
        print(key,value)

if __name__ == "__main__":
    main()

