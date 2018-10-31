# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/10/31-9:22 AM
@file: sleep.py
@function: 暂停一秒输出。
'''
import time

myDir = {1: 'a', 2: 'b'}
for key, value in dict.items(myDir):
    print(key, value)
    time.sleep(1)  # 暂停一秒
