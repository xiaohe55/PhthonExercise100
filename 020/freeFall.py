# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/16-9:32 AM
@file: freeFall.py
@function: 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

sumhig = 100
hn = sumhig / 2
for i in range(2, 11):
    sumhig += 2 * hn
    hn /= 2
    print("第%d次下落，总高度%s" % (i, sumhig))
    print("第{}次下落，此时高度{}".format(i, hn))
print("总高度：", sumhig)
print("此时高度：", hn)
