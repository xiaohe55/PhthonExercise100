# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/20-9:49 AM
@file: diamond.py
@function: 打印菱形
   *
  ***
 *****
*******
 *****
  ***
   *
'''

for i in range(4):
    # print(i)
    for j in range(2 - i + 1):
        print(" ", end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
for i in range(3):
    for j in range(i + 1):
        print(' ', end='')
    for k in range(4 - 2 * i + 1):
        print('*', end='')
    print()
