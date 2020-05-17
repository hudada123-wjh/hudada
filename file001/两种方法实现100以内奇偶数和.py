#-*- coding: utf-8 -*-\
# 奇数和。
s = 0
for i in range(1,100):
    if i % 2 :
        s = i + s
        if s > 1000:
            break
print(s)
print(i)

s = 0
i = 1
while i < 100:
    if i % 2:
        s += i
        if s > 1000:
            break
    i = i + 1
print(i)
print(s)


# 偶数和：
s = 0
for i in range(1,100):
    if i % 2:
        s += i
        s += 1
print(s)


