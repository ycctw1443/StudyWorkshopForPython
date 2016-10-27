#!/usr/bin/env python
# -*- coding:utf-8 -*-

def main():
    print("秒を入力してください：")
    second = int(input())
    hour = second // 3600
    minute = (second  // 60) - hour * 60
    seconds = second - minute * 60 - hour * 3600
    print("%d秒は%d時間%d分%d秒です" % (second,hour,minute,seconds))

if __name__ == "__main__":
    main()
    

