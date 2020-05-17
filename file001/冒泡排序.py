# -*- coding:utf-8 -*-
# @Time:2020/5/16 22:59
# @Author:whweia
# @File:冒泡排序.py
# a = [55,17,100,66,99,1]
# s = len(a)
# for i in range(s-1):
#     for j in range(s - i - 1):
#         print("比较",a[j],":",a[j+1])
#         print("比较",j,":",j+1)
#         if a[j] > a[j + 1]:
#             a[j],a[j + 1] = a[j + 1],a[j]
#     print(a)




a = [10,4,2,3,5,1,7]
b = len(a)
for i in range(b - 1):
    for j in range(b - i -1):
        if a[j] > a [j + 1]:
            a[j],a[j + 1] = a[j + 1],a[j]
print(a)








a = [12,5,2,7,5,1]
s = len(a)
for i in range(s - 1):
    for j in range(s - i - 1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j + 1],a[j]
print(a)
















