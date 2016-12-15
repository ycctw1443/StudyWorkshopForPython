#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import codecs
import re
import math
import MeCab

class Student(object):

    def __init__(self,student_id,name,math,japanese,fm):
        self.student_id = student_id 
        self.name = name 
        self.math = math
        self.japanese = japanese
        self.fm = fm


class Classroom(object):

    def __init__(self,grade,class_id,student_list,teacher):
        self.grade = grade
        self.class_id = class_id
        self.student_list = student_list
        self.teacher = teacher

    def getSumAvg(self):
        math_point_list = [int(student.math) for student in self.student_list]
        sum_math_point = sum(math_point_list)
        japanese_point_list = [int(student.math) for student in self.student_list]
        sum_japanese_point = sum(japanese_point_list)
       
        return (sum_math_point + sum_japanese_point)  / len(self.student_list) 
    
    def getMaxPoint(self):
        sum_point_list =  [int(student.math) + int(student.japanese) for student in self.student_list]
        return max(sum_point_list)


class Teacher(object):

    def __init__(self,name,grade,class_id,subject,mail,extension_num,phone_num,profile,url):
        self.name = name
        self.grade = grade 
        self.class_id = class_id
        self.subject = subject
        self.mail = mail
        self.extension_num = extension_num
        self.phone_num = phone_num
        self.profile = profile
        self.url = url

    def printTeacherData(self):
        print("名前:",self.name)
        print("担任の学年:",self.grade)
        print("担任のクラス:",self.class_id)
        print("担当教科:",self.subject)

    def printMailAddress(self):
        print("メールアドレス:",self.mail[0])
        if(len(self.mail) >= 2):
             print("個人用メールアドレス",self.mail[1])

    def printUrl(self):
        print("URL1:",self.url[0])
        if(len(self.url) >= 2):
            print("URL2:",self.url[1])

    def printPhoneNum(self):
        print("電話場号:",self.phone_num)

    def analyzeProfile(self):
        mecab = MeCab.Tagger("-Ochasen")
        print(mecab.parse(self.profile))


def main():
    
    class1_1 = readClassData(1,1)
    class1_2 = readClassData(1,2)

    compareAvgScore(class1_1,class1_2)
    compareMaxScore(class1_1,class1_2)
   
    print("\n")

    class1_1.teacher.printTeacherData()
    class1_1.teacher.printMailAddress()
    class1_1.teacher.printPhoneNum()
    class1_1.teacher.printUrl()
   
    print("\n")
   
    class1_2.teacher.printTeacherData()
    class1_2.teacher.printMailAddress()
    class1_2.teacher.printPhoneNum()
    class1_2.teacher.printUrl()

    print("\n")
    #class1_1.teacher.analyzeProfile()
    #class1_2.teacher.analyzeProfile()

    extractionWodsParts()

def readClassData(grade,class_id):
    
    file_name = "./" + str(grade) + "-" + str(class_id) + ".csv"
    tmp = []
    text_data = codecs.open(file_name,"r","utf-8")
    try:
        for l in text_data:
            l = l.strip()
            l = re.split(",",l)
            tmp.append(l)
    except: 
        print("FILE_READ_ERROR")
    finally:
        text_data.close()

    student_list = []
    for i in tmp[2::]:
        student = Student(i[0],i[1],i[2],i[3],i[4])
        student_list.append(student)

    teacher_name = tmp[1][1].lower()
    teacher = readTeacherData(teacher_name)
    
    return Classroom(int(grade),int(class_id),student_list,teacher)


def readTeacherData(name):

    file_name = "./" + str(name) + ".txt"
    tmp = []
    text_data = codecs.open(file_name,"r","utf-8")
    try:
        for l in text_data:
            l = l.strip()
            tmp.append(l)
    except: 
        print("FILE_READ_ERROR")
    finally:
        text_data.close()
    
    tmp = tmp[1::2]
    mail_pattern = re.compile(r"[A-Za-z0-9\-\.\_]+@[A-Za-z0-9\-\_]+\.[A-Za-z0-9\-\.\_]+")
    tmp[3] = mail_pattern.findall(tmp[3])

    grade = int(tmp[1][0:1])
    class_id = int(tmp[1][2:3])

    extention_pattern = re.compile(r"\d{4}")
    extention_num = extention_pattern.search(tmp[4]).group()
    phone_num_pattern = re.compile(r"\d{11}|\d{3}-\d{4}-\d{4}")
    phone_num = phone_num_pattern.findall(tmp[4])

    url_pattern =  re.compile(r"https?://[A-Za-z0-9/:%#\$&\?\(\)~\.=\+\-]+")
    tmp[6] = url_pattern.findall(tmp[6])
    
    return Teacher(tmp[0],grade,class_id,tmp[2],tmp[3],extention_num,phone_num[0],tmp[5],tmp[6])


def compareAvgScore(classroom1, classroom2):
    if(classroom1.getSumAvg() > classroom2.getSumAvg()):
        winclass = classroom1
    elif  (classroom1.getSumAvg() < classroom2.getSumAvg()):
        winclass = classroom2
    else:
        print("平均点は同点です")
        return

    print("平均点は",winclass.teacher.name, "の勝ちです")


def compareMaxScore(classroom1,classroom2):
    if(classroom1.getMaxPoint() > classroom2.getMaxPoint()):
        winclass = classroom1
    elif (classroom1.getMaxPoint() < classroom2.getMaxPoint()):
        winclass = classroom2
    else: 
        print("最高得点は同じです")
        return
    print("最高点は",winclass.teacher.name,"の勝ちです")


def extractionWodsParts():
    mecab = MeCab.Tagger()
    extractionDic = {}
    node = mecab.parseToNode("私はペンです")
    while(node):
        data = node.feature.split(",")
        if(data[0] == "名詞"):
            extractionDic[node.surface] = extractionDic.get(node.surface, 0) + 1
        node = node.next

    print(extractionDic)

if __name__ == '__main__':
    main()

