# -*- coding: utf-8 -*-

"""
@author: heyongkang
@create: 2018/11/3-10:57 AM
@file: factorization.py
@function: 将一个正整数分解质因数。输入90,打印出90=2*3*3*5
"""


def divPrime(num):
    lt = []
    print(num, '=', end=' ')
    while num != 1:
        for i in range(2, int(num + 1)):
            if num % i == 0:  # i是num的一个质因数
                lt.append(i)
                num = num / i  # 将num除以i，剩下的部分继续分解
                break
    for i in range(0, len(lt) - 1):
        print(lt[i], '*', end=' ')

    print(lt[-1])

divPrime(18)