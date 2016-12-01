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


def main():
   # student = Student()
   # classroom = Classroom()
   # print(student, classroom)
    class1_1 = readClassData(1,1)
    class1_2 = readClassData(1,2)
    
    ave_var_sta(class1_1.student_list,class1_2.student_list)

   # print(class1_1.teacher_name)
   # print(class1_2.teacher_name)


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


    return Classroom(1,1,student_list,tmp[1][1],tmp[1][4])


   # print(tmp)


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


if __name__ == '__main__':

    tmp = []
    main()

