#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    print("分を入力してください：")
    minute = float(input())
    seconds = minute * 60
    hour = seconds // 3600
    minutes = (seconds  // 60) - hour * 60
    second = seconds - minutes * 60 - hour * 3600
    print("%d分は%d時間%d分%d秒です" % (minute,hour,minutes,second))

if __name__ == "__main__":
    main()
    

