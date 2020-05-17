# -*- coding:utf-8 -*-
# @Time:2020/5/16 23:21
# @Author:whweia
# @File:遍历知识.py
a = {
    "name":"hahaha",
    "password":"123456"
     }
print(a)
print(a.keys())
print(a.values())
print(a["password"])
for i in a.keys():
    print(i)
    print(a[i])
for j in a.values():
    print(j)
