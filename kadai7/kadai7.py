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
   # student = Student()
   # classroom = Classroom()
   # print(student, classroom)
    class1_1 = readClassData(1,1)
    class1_2 = readClassData(1,2)
    
    print(class1_1.teacher_name)
    print(class1_2.teacher_name)

<<<<<<< HEAD

=======
>>>>>>> 2deb4a3... 問題１終わり！
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


    

if __name__ == '__main__':

    tmp = []
    main()

