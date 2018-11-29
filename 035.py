# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/29-8:23 AM
@file: 035.py
@function: 文本颜色设置。
'''


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(bcolors.WARING + '颜色' + bcolors.ENDC)
