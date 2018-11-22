# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/22-9:51 AM
@file: 030.py
@function: 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''

a = input("请输入一串数字：")
print(a)
print(type(a))
b = a[::-1]
print(b)
print(type(b))
if a == b:
    print("Y")
else:
    print("N")
