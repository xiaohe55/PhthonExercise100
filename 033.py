# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/28-10:02 AM
@file: 033.py
@function: 按逗号分隔列表。
'''
L = [1, 2, 3, 4, 5]
print(L)
# 方法一：
# L = repr(L)[1:-1]

for i in range(len(L)):
    if i != len(L) - 1:
        print(L[i], end=',')
    else:
        print(L[i])
