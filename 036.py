# -*- coding: utf-8 -*-

'''
@author: coyote
@create: 2018/11/29-11:43 AM
@file: 036.py
@function: 求100之内的素数。
'''

low = int(input("请输入比较小的数："))
upper = int(input("请输入比较大的数："))
for i in range(low, upper):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
