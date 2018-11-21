# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/21-9:39 AM
@file: qiujiecheng.py
@function: 求1+2!+3!+...+20!的和。
'''


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


s = 0
for i in range(1, 21):
    s += fac(i)
print(s)
