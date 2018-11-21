# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/21-9:44 AM
@file: jiecheng.py
@function: 利用递归方法求5!。
'''


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n - 1)


print(fac(5))
