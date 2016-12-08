#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import re
import math

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

def main():
    
    class1_1 = readClassData(1,1)
    class1_2 = readClassData(1,2)

    teacher_mio  = readTeacherData("mio")

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

    url_pattern =  re.compile(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    tmp[6] = url_pattern.findall(tmp[6])
    
    return Teacher(tmp[0],grade,class_id,tmp[2],tmp[3],extention_num,phone_num,tmp[5],["url_1","url_2"])

   # print(tmp[6])


   
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
    
def ave_var_sta(student_list1, student_list2):

    student1_1_len = len(student_list1)
    student1_2_len = len(student_list2)

    student1_1_math = [int(student.math) for student in student_list1]
    student1_1_math_male = [int(student.math) for student in student_list1 if student.fm == "M"]
    student1_1_math_female = [int(student.math) for student in student_list1 if student.fm == "F"]
    student1_1_japanese = [int(student.japanese) for student in student_list1]
    student1_1_japanese_male = [int(student.japanese) for student in student_list1 if student.fm == "M"]
    student1_1_japanese_female = [int(student.japanese) for student in student_list1 if student.fm == "F"]
    student1_2_math = [int(student.math) for student in student_list2]
    student1_2_math_male = [int(student.math) for student in student_list2 if student.fm == "M"]
    student1_2_math_female = [int(student.math) for student in student_list2 if student.fm == "F"]
    student1_2_japanese = [int(student.japanese) for student in student_list2]
    student1_2_japanese_male = [int(student.japanese) for student in student_list2 if student.fm == "M"]
    student1_2_japanese_female = [int(student.japanese) for student in student_list2 if student.fm == "F"]

    student1_1_male_len = len(student1_1_math_male)
    student1_1_female_len = len(student1_1_math_female)
    student1_2_male_len = len(student1_2_math_male)
    student1_2_female_len = len(student1_2_math_female)

    student1_1_math_sum = sum(student1_1_math)
    student1_1_math_male_sum = sum(student1_1_math_male)
    student1_1_math_female_sum = sum(student1_1_math_female)
    student1_1_japanese_sum = sum(student1_1_japanese)
    student1_1_japanese_male_sum = sum(student1_1_japanese_male)
    student1_1_japanese_female_sum = sum(student1_1_japanese_female)
    student1_2_math_sum = sum(student1_2_math)
    student1_2_math_male_sum = sum(student1_2_math_male)
    student1_2_math_female_sum = sum(student1_2_math_female)
    student1_2_japanese_sum = sum(student1_2_japanese)
    student1_2_japanese_male_sum = sum(student1_2_japanese_male)
    student1_2_japanese_female_sum = sum(student1_2_japanese_female)

    student1_1_sum = student1_1_math_sum + student1_1_japanese_sum
    student1_1_male_sum = student1_1_math_male_sum + student1_1_japanese_male_sum
    student1_1_female_sum = student1_1_math_female_sum + student1_1_japanese_female_sum
    student1_2_sum = student1_2_math_sum + student1_2_japanese_sum
    student1_2_male_sum = student1_2_math_male_sum + student1_2_japanese_male_sum
    student1_2_female_sum = student1_2_math_female_sum + student1_2_japanese_female_sum
    allstudent_sum = student1_1_sum + student1_2_sum

    student1_1_ave = student1_1_sum / (student1_1_len * 2)
    student1_1_male_ave = student1_1_male_sum / (student1_1_male_len * 2)
    student1_1_female_ave = student1_1_female_sum / (student1_1_female_len * 2)
    student1_2_ave = student1_2_sum / (student1_2_len * 2)
    student1_2_male_ave = student1_2_male_sum / (student1_2_male_len * 2)
    student1_2_female_ave = student1_2_female_sum / (student1_2_female_len * 2)
    allstudent_ave = (student1_1_ave + student1_2_ave) / 2
    allstudent_male_ave = (student1_1_male_ave + student1_2_male_ave) / 2
    allstudent_female_ave = (student1_1_female_ave + student1_2_female_ave) / 2
    print(student1_1_ave,student1_2_ave,allstudent_ave,allstudent_male_ave,allstudent_female_ave)

    allsum = 0
    sum1_1 = 0
    for m in student1_1_math:
        m = (m - student1_1_ave) ** 2
        sum1_1 += m
        allsum += m
    for j in student1_1_japanese:
        j = (j - student1_1_ave) ** 2
        sum1_1 += j
        allsum += j
    student1_1_var = sum1_1 / (student1_1_len * 2)
    print(student1_1_var)
    student1_1_sta = math.sqrt(student1_1_var)
    print(student1_1_sta)

    sum1_2 = 0
    for m in student1_2_math:
        m = (m - student1_2_ave) ** 2
        sum1_2 += m
        allsum += m
    for j in student1_2_japanese:
        j = (j - student1_2_ave) ** 2
        sum1_2 += j
        allsum += j
    student1_2_var = sum1_2 / (student1_2_len * 2)
    print(student1_2_var)
    student1_2_sta = math.sqrt(student1_2_var)
    print(student1_2_sta)

    allstudent_var = allsum / ((student1_1_len + student1_2_len) * 2)
    print(allstudent_var)
    allstudent_sta = math.sqrt(allstudent_var)
    print(allstudent_sta)

    sum_male = 0
    for m in student1_1_math_male:
        m = (m - allstudent_male_ave) ** 2
        sum_male += m
    for j in student1_1_japanese_male:
        j = (j - allstudent_male_ave) ** 2
        sum_male += j
    for m in student1_2_math_male:
        m = (m - allstudent_male_ave) ** 2
        sum_male += m
    for j in student1_2_japanese_male:
        j = (j - allstudent_male_ave) ** 2
        sum_male += j
    allstudent_male_var = sum_male / ((student1_1_male_len + student1_2_male_len) * 2)
    print(allstudent_male_var)
    allstudent_male_sta = math.sqrt(allstudent_male_var)
    print(allstudent_male_sta)

    sum_female = 0
    for m in student1_1_math_female:
        m = (m - allstudent_female_ave) ** 2
        sum_female += m
    for j in student1_1_japanese_female:
        j = (j - allstudent_female_ave) ** 2
        sum_female += j
    for m in student1_2_math_female:
        m = (m - allstudent_female_ave) ** 2
        sum_female += m
    for j in student1_2_japanese_female:
        j = (j - allstudent_female_ave) ** 2
        sum_female += j
    allstudent_female_var = sum_female / ((student1_1_female_len + student1_2_female_len) * 2)
    print(allstudent_female_var)
    allstudent_female_sta = math.sqrt(allstudent_female_var)
    print(allstudent_female_sta)


def mondai2(student_list,grade,class_id):
    name = [i.name for i in student_list]
    math = [int(i.math) for i in student_list]
    japanese = [int(i.math) for i in student_list]
    total = [int(i.math)+int(i.japanese) for i in student_list]
    print("class:",grade,"-",class_id)
    print("math=",name[math.index(max(math))],
          ",japanese=",name[japanese.index(max(japanese))],
          ",total=",name[total.index(max(total))])

def mondai3(list1,list2):
    all_list = list1 + list2
    name = [i.name for i in all_list]
    math = [int(i.math) for i in all_list]
    japanese = [int(i.japanese) for i in all_list]
    total = [int(i.math)+int(i.japanese) for i in all_list]
    print("all classes on grade 1")
    print("math=",name[math.index(max(math))])
    print("japanese=",name[japanese.index(max(japanese))])
    print("total=",name[total.index(max(total))])
    return all_list

def mondai4(list1,list2):
    all_list = mondai3(list1,list2)
    name_f = [i.name for i in all_list if i.fm == "F"]
    name_m = [i.name for i in all_list if i.fm == "M"]                         
    math_f = [int(i.math) for i in all_list if i.fm == "F"] 
    math_m = [int(i.math) for i in all_list if i.fm == "M"]
    japanese_f = [int(i.japanese) for i in all_list if i.fm == "F"]
    japanese_m = [int(i.japanese) for i in all_list if i.fm == "M"]
    total_f = [int(i.math)+int(i.japanese) for i in all_list if i.fm == "F"]
    total_m = [int(i.math)+int(i.japanese) for i in all_list if i.fm == "M"]
    print("by f/m")
    print("female math=",name_f[math_f.index(max(math_f))])
    print("female japanese=",name_f[japanese_f.index(max(japanese_f))])
    print("female total=",name_f[total_f.index(max(total_f))])
    print("male math=",name_m[math_m.index(max(math_m))])
    print("male japanese=",name_m[japanese_m.index(max(japanese_m))])
    print("male total=",name_m[total_m.index(max(total_m))])


#--------課題8------------#


if __name__ == '__main__':
    main()

