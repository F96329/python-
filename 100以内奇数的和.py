# 求100以内所有的奇数之和
i = 0
b = 0
while i < 99 :
    i += 1
    if i % 2 != 0 :        
        b += i
else:
    print(b)