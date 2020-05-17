#-*- coding: utf-8 -*-
'''
def add(a,b):
    return(a + b)
def ajj(a,b):
    return(a - b)
def axx(a,b):
    return(a * b)
def acc(a,b):
    return(a / b)
print("请选择一个值：1加/2减/3乘/4除")
s = int(input("请输入1234算法："))
n1 = float(input("第一个数字为："))
n2 = float(input("第二个数字为："))
# for i in range(1,4):
if s == 1:
    c = add(n1,n2)
    print(c)
elif s == 2:
    c = ajj(n1,n2)
    print(c)
elif s == 3:
    c = axx(n1,n2)
    print(c)
elif s == 4:
    c = acc(n1,n2)
    print(c)
else:
    print("没了")
  '''

def add(a,b):
    return(a+b)
def ajj(a,b):
    return (a - b)
def axx(a,b):
    return (a * b)
def acc(a,b):
    return (a / b)
print("1代表加，2代表减，3代表乘，4代表除。")
s = int(input("请输入1234算法："))
while s == 1 or s == 2 or s == 3 or s == 4:
    n1 = float(input("请输入第一个值："))
    n2 = float(input("请输入第二个值："))
    if s == 1:
        print(add(n1,n2))
    elif s == 2:
        print(ajj(n1,n2))
    elif s == 3:
        print(axx(n1,n2))
    elif s == 4:
        print(acc(n1,n2))
    else:
        print("调皮")







