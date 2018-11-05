# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/5-11:03 PM
@file: ifElse.py
@function: 条件运算符
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

num = int(input("请输入成绩："))
if num >= 90:
    print("A")
elif num >= 60:
    print("B")
else:
    print("C")
