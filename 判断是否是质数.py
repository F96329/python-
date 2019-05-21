# 练习4：    
#     获取用户输入的任意数，判断其是否是质数。质数是只能被1和它自身整除的数，1不是质数也不是合数。
a = int(input('请输入你想判断的大于1的整数:'))
if a <= 1 :
    print('输入不合法，请输入大于1的整数')
i = 2 
flag = True
while i < a :
    if a % i == 0 :
        flag = False
    i += 1
if flag :
    print(a,'是质数')
else :
    print(a,'不是质数')