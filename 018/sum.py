#-*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/15-11:13 AM
@file: sum.py
@function: 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''

n = int(input("请输入个数："))
a = int(input("请输入数字："))
li= []
tn = 0
for i in range(n):
    tn = tn + a
    a = a * 10
    li.append(tn)
    print(tn)
print(sum(li))
