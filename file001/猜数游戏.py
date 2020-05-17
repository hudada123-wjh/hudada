# -*- coding:utf-8 -*-
# @Time:2020/5/16 22:44
# @Author:whweia
# @File:猜数游戏.py
import random
key = random.randint(1,20)
while 1:
    i = int(input("请输入一个数："))
    if i > key:
        print("太大了")
    elif i < key:
        print("太小了")
    elif i == key:
        print("答对了")
