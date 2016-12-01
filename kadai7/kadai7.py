#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import re


class Student(object):

    def __init__(self,student_id,name,math,japanese,fm):
        self.student_id = student_id 
        self.name = name 
        self.math = math
        self.japanese = japanese
        self.fm = fm


class Classroom(object):

    def __init__(self,grade,class_id,student_list,teacher_name,teacher_fm):
        self.grade = grade
        self.class_id = class_id
        self.student_list = student_list
        self.teacher_name = teacher_name
        self.teacher_fm = teacher_fm


def main():
    
    class1_1 = readClassData(1,1)
    class1_2 = readClassData(1,2)
    

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

    return Classroom(int(grade),int(class_id),student_list,tmp[1][1],tmp[1][4])

   
def sortSumPointOneClass(student_list):
    list = sorted(student_list,key=lambda x: int(x.japanese + x.math), reverse=True)
    for student in list:
        print(student.name , student.japanese,student.math)


def sortSumPointAllClass(student_list_1,student_list_2):
    list = student_list_1 + student_list_2 
    list = sorted(list,key=lambda x: int(x.japanese + x.math), reverse=True)
    for student in list:
         print(student.name , student.japanese,student.math)


def sortSumPointMF(student_list_1,student_list_2):
    allstudent_list = student_list_1 + student_list_2
    male_list = [student for student in allstudent_list if student.fm == "M"]  
    female_list = [student for student in allstudent_list if student.fm == "F"] 
    
    male_list = sorted(male_list,key=lambda x: int(x.japanese + x.math), reverse=True)
    female_list = sorted(female_list,key=lambda x: int(x.japanese + x.math), reverse=True)
   
    for student in male_list:
        print(student.name, student.japanese, student.math, student.fm)
    for student in female_list:
        print(student.name, student.japanese, student.math, student.fm)
    


if __name__ == '__main__':
    main()

