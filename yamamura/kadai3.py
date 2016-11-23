#!/usr/bin/env python
# -*- coding:utf-8 -*-



def main():
    print('秒を入力してください')
    s = int(input())
    print('%d秒は' % s, end='')
    hr = s // 3600
    print('%d時間' % hr, end='')
    mi = (s - hr * 3600) // 60
    print('%d分' % mi, end='')
    se = (s - hr * 3600 - mi * 60) % 60
    print('%d秒です。' % se)


if __name__ == '__main__':
    main()
