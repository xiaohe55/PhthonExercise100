# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/3-9:51 AM
@file: PrimeNum.py
@function:判断101-200之间有多少个素数，并输出所有素数。
'''

result = []
flag = 1
count = 0
for n in range(100, 201):
    for i in range(2, n):
        if n % i == 0:
            flag = 0
            break
    if flag == 1:
        result.append(n)
        count += 1
    flag = 1
print(result)
print(count)
