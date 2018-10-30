#-*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/10/29-9:10 PM
@file: Fibonacci.py
@function: 斐波那契数列
'''
def fib(n):
    resule = []
    a,b = 0,1
    for i in range(n):
        resule.append(b)
        a,b=b,a+b
    return resule
print fib(input("please input num:"))
