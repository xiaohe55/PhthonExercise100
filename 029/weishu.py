# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/22-9:44 AM
@file: weishu.py
@function: 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
num = list(input("请输入最多5位数："))
print(num)
print(type(num))
print(len(num))
num.reverse()
for i in range(len(num)):
    print(num[i], end='')
