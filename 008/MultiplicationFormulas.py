# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/10/30-9:42 AM
@file: MultiplicationFormulas.py
@function: 输出 9*9 乘法口诀表
'''

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d\t" % (i, j, j * i), end='')
    print()
