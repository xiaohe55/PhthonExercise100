#-*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/10/30-9:34 AM
@file: copyList.py
@function: 将一个列表的数据复制到另一个列表中。
'''

a=[1,2,3,4]
b=a[:]
print b
a.append(5)
print a
print b


