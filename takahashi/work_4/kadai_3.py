
#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
import collections


def main():
    inputDeta = sys.argv
    tmp = inputDeta[1].split(",")
    staffNum = int(tmp[0]);
    semistaffNum = len(tmp) - staffNum - 1
    staffOkDay = tmp[1:staffNum+1]
    semistaffOkDay = tmp[staffNum+1::]

    staffOkDay = [i.split("-") for i in staffOkDay]

    if semistaffNum > 0 :   
        semistaffOkDay = [i.split("-") for i in semistaffOkDay]  

    staffOkDay = [i for i2 in staffOkDay for i in i2]
    semistaffOkDay = [i for i2 in semistaffOkDay for i in i2]
    
    staffOkDayNumList = collections.Counter(staffOkDay)
    semistaffOkDayNumList = collections.Counter(semistaffOkDay)
   
    allOkNumList = getOkDaySum(staffOkDayNumList,semistaffOkDayNumList)
    allOkNumList = leaveMaxDay(allOkNumList) 
    okDay = min(allOkNumList,key=lambda x:x[0])
    print(okDay) 
        

def getOkDaySum(staffOkNumList,semistaffOkNumList):
    if len(semistaffOkNumList) == 0:
        return staffOkNumList
    allStaffOkDayNum = {}

    #allStaffOkDayNum = [i for i in staffOkNumList if i in semistaffOkNumList]
    for key in semistaffOkNumList:
         if key in staffOkNumList:      
            allStaffOkDayNum[key] = semistaffOkNumList[key] + staffOkNumList[key]
    print(allStaffOkDayNum)
    return allStaffOkDayNum


def leaveMaxDay(okDayList):
    okDayList =  sorted(okDayList.items(),key=lambda x:x[1],reverse = True)
    for index,item in  enumerate(okDayList):
        if item[1] != okDayList[0][1]:
            okDayList = okDayList[0:index]
            break
   
    return okDayList

if __name__ == '__main__':
    main()
