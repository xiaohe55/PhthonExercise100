# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/27-9:34 AM
@file: 031.py
@function: 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
'''

weeklist = {'M': 'Monday', 'T': {'u': 'Tuesday', 'h': 'Thursday'}, 'W': 'Wednesday', 'F': 'Friday',
            'S': {'a': 'Saturday', 'u': 'Sunday'}}
sLetter1 = input("请输入首字母：")
sLetter1 = sLetter1.upper()

if sLetter1 in ['T', 'S']:
    sLetter2 = input("请输入第二个字母：")
    print(weeklist[sLetter1][sLetter2])
else:
    print(weeklist[sLetter1])
