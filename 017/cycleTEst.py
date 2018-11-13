#-*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/13-9:48 AM
@file: cycleTEst.py
@function: 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''
alpha = 0
digit = 0
space = 0
other = 0
a= input("请输入字符串：")
for i in a:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        other += 1

print("char = %d, space = %d, digit = %d, other = %d" %(alpha,space,digit,other))
