#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def main():
    print('秒を入力してください:')
    inputSec = int(input())
    sec = inputSec
    hour = inputSec//3600
    sec -= 3600*hour

    minn = sec//60
    sec -= 60*minn

    print('%d分は%d時間%d分%d秒です' % (inputSec,hour,minn,sec));    
 
if __name__ == '__main__':
    main()
