#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def main():
    print('分を入力してください:')
    inputMin = float(input())*60
    sec = inputMin
    hour = sec//3600
    sec -= 3600*hour

    minn = sec//60
    sec -= 60*minn

    print('%d病は%d時間%d分%d秒です' % (inputMin,hour,minn,sec));    
 
if __name__ == '__main__':
    main()
