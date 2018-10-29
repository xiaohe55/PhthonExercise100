#-*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/10/29-8:52 PM
@file: reverse.py
@function: 输入三个整数x,y,z，请把这三个数由小到大输出。
'''

l=[]
for i in range(3):
    x = input("请输入%d个整数:"%i)
    l.append(x)
l.sort()
print l