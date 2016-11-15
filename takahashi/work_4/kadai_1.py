#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def main():

    fruits = ["apple", "orange", "lemon", "strawberry", "apple", "cherry", "melon", "apple", "lemon"]
    print(1, fruits)
    disp1(fruits)
    print(1, fruits)
    disp2(fruits)
    print(1, fruits)
    disp3(fruits)
    print(1, fruits)
    disp4(fruits)
    print(1, fruits)
    disp5(fruits)

def disp1(b):
    a = b
    print(a[::-1])


def disp2(b):
    a = {}
    a = b
    for index, st in enumerate(a):
        a[index] = st[::-1]
    print(a)

def disp3(b):
    a = {}
    a = b
    for index, st in enumerate(a):
        tmp = a.count(a[index])
        a[index] = a[index] + ":" +str(tmp)
    print(a)

def disp4(b):
    a = []
    a = b
    for index,st in enumerate(a):
        tmp = len(a[index])
        a[index] = a[index] + ":" + str(tmp)
    print(a)
        
def disp5(b):
    a = []
    a = b
    dic = {} 
    for index, st in enumerate(a):
         dic.update({st : len(a[index:])})
    dic = sorted(dic.items(),key=lambda x:x[0])
    print(dic)

if __name__ == '__main__':
    main()
