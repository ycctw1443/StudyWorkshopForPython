
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

    for index, item in enumerate(staffOkDay):
        staffOkDay[index] =  staffOkDay[index].split("-")
    if semistaffNum > 0 :   
       for index, item in enumerate(semistaffOkDay):
             semistaffOkDay[index] = semistaffOkDay[index].split("-")
    

    staffOkDay = getOkDayList(staffOkDay)
    semistaffOkDay = getOkDayList(semistaffOkDay)
    
    staffOkDayNumList = collections.Counter(staffOkDay)
    semistaffOkDayNumList = collections.Counter(semistaffOkDay)
   
    allOkNumList = getOkDaySum(staffOkDayNumList,semistaffOkDayNumList)
    allOkNumList = leaveMaxDay(allOkNumList) 
    okDay = min(allOkNumList,key=lambda x:x[0])
    print(okDay) 
        

 # List[item[1,2,3],item[4,5,6]...] to List[k1,2,3,4,5,6...]
def getOkDayList(staffOkDayList):
    tmp = []
    for item in staffOkDayList: 
        for item2 in item:
            tmp.append(item2)
    return tmp

def getOkDaySum(staffOkNumList,semistaffOkNumList):
    if len(semistaffOkNumList) == 0:
        return staffOkNumList
    allStaffOkDayNum = {}
    for key in semistaffOkNumList:
         if key in staffOkNumList:      
            allStaffOkDayNum[key] = semistaffOkNumList[key] + staffOkNumList[key]
   
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
