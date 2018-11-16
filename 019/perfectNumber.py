# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/15-11:28 AM
@file: perfectNumber.py
@function: 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

for i in range(2, 2000):
    li = []
    for j in range(1, i):
        if i % j == 0:
            li.append(j)
    num = sum(li)
    if num == i:
        print(i)
