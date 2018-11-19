# -*- coding: utf-8 -*-

'''
@author: heyongkang
@create: 2018/11/19-9:39 AM
@file: pingPangGame.py
@function: 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
'''
for i in range(ord('x'), ord('z') + 1):
    for j in range(ord('x'), ord('z') + 1):
        for k in range(ord('x'), ord('z') + 1):
            if i != j and j != k and k != i:
                if i != ord('x') and k != ord('x') and k != ord('z'):
                    print("a的对手是{},b的对手是{},c的对手是{}".format(chr(i), chr(j), chr(k)))
