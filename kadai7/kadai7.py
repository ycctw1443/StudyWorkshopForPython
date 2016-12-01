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

    mondai2(class1_1.student_list,class1_1.grade,class1_1.class_id)
    mondai2(class1_2.student_list,class1_2.grade,class1_2.class_id)
    mondai4(class1_1.student_list,class1_2.student_list)

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

    return Classroom(grade,class_id,student_list,tmp[1][1],tmp[1][4])

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

if __name__ == '__main__':
    main()

