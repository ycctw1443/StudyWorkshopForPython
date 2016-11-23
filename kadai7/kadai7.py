#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self):
        self.student_id = None
        self.name = None
        self.math = None
        self.japanese = None
        self.fm = None


class Classroom(object):

    def __init__(self):
        self.grade = None
        self.class_id = None
        self.student_list = None
        self.teacher_name = None
        self.teacher_fm = None


def main():
    student = Student()
    classroom = Classroom()
    print(student, classroom)

if __name__ == '__main__':
    main()

