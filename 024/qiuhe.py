# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/21-9:32 AM
@file: qiuhe.py
@function: 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''

a = 2
b = 1
s = 0
for i in range(1, 21):
    s += a / b
    b, a = a, a + b
print(s)
