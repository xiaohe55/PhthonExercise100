# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/5-11:09 PM
@file: riqi.py
@function: 输出指定格式的日期
'''
import datetime

# 格式化日期
print(datetime.date.today().strftime("%d/%m/%Y"))

birthDay = datetime.date(1922, 1, 12)
print(birthDay.strftime("%d/%m/%Y"))

# 天数加1
print(birthDay + datetime.timedelta(days=1))

# 日期替换
print(birthDay.replace(year=birthDay.year + 1))
