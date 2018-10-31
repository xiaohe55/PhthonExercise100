# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/10/31-9:43 AM
@file: rabbit.py
@function: 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
还是斐波那契堆 和第6题一样
'''


def feb(n):
    # result = []
    a, b = 0, 1
    for i in range(n):
        # result.append(b)
        a, b = b, a + b
    return a


print(feb(int(input("第几个月的兔子"))))
