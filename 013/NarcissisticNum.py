# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/3-10:29 AM
@file: NarcissisticNum.py
@function: 水仙花数是指一个 3位正整数，它的每个位上的数字的 3 次幂之和等于它本身。（例如：1^3 + 5^3+ 3^3 = 153）
'''

for i in range(152, 1000):
    a = int(i / 100)
    b = int(i / 10 % 10)
    c = int(i % 10)
    d = a ** 3 + b ** 3 + c ** 3
    if d == i:
        print(i)
