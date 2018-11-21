# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/21-9:46 AM
@file: diguifanxu.py
@function: 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


def outPut(s, l):
    if l == 0:
        return
    print(s[l - 1])
    outPut(s, l - 1)


s = input("请输入字符串：")
l = len(s)
outPut(s, l)
