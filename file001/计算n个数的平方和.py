# -*- coding:utf-8 -*-
# @Time:2020/5/17 17:01
# @Author:whweia
# @File:计算n个数的平方和.py
import random
def sum111111(n):
    sum = 0
    for i in range(1,n+1):
        sum += i * i                 # sum = sum + i * i
    return sum        # 每循环一次返回sum值

#调用函数
n = random.randint(1,100)
print(n)
print(sum111111(n))
