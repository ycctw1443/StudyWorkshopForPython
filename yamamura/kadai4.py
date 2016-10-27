#!/usr/bin/env python
# -*- coding:utf-8 -*-



def main():
    print('分を入力してください')
    m = float(input())
    s = m * 60
    print('%f分は' % m, end='')
    hr = s // 3600
    print('%d時間' % hr, end='')
    mi = (s - hr * 3600) // 60
    print('%d分' % mi, end='')
    se = (s - hr * 3600 - mi * 60) % 60
    print('%d秒です' % se)


if __name__ == '__main__':
    main()
