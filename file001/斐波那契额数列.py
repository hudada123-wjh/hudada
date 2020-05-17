# -*- coding:utf-8 -*-
# @Time:2020/5/17 15:33
# @Author:whweia
# @File:斐波那契额数列.py
# n = int(input("打印多少项："))
# n1 = 1 # 第一项
# n2 = 1 # 第二项
# count = 2 # 每两项的和
# if n <= 0:
#     print("请输入正整数：")
# elif n == 1:
#     print(n1)
# else:
#     print("斐波那契数列为：")
#     print(n1,n2,end = " ")         # 先打印前两项，要不换行
#     while count < n:                   # 如果输入值大于count停止
#         n3 = n1 + n2                   # 开始计算和,保存到n3中
#         print(n3,end = " ")            # 打印n3，使用end不换行
#         n1 = n2
#         n2 = n3
#         count += 1


n = int((input("你需要几项：")))
n1 = 1
n2 = 1
count = 2
if n <= 0:
    print("请输入正整数")
elif n == 1:
    print(n1)
else:
    print("斐波那契数列为：")
    print(n1, n2, end=" ")
    while count < n:
        n3 = n1 + n2
        print(n3,end = " ")
        n1 = n2
        n2 = n3
        count += 1




