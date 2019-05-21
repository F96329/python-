#  从键盘输入小明的期末成绩:
#             当成绩为100时，'奖励一辆BMW'
#             当成绩为[80-99]时，'奖励一台iphone'
#             当成绩为[60-79]时，'奖励一本参考书'
#             其他时，什么奖励也没有
Grade = float(input('请输入小明的成绩'))
if 0 <= Grade <= 100:
    if Grade == 100 :
        print('小明的奖励是一辆宝马')
    elif Grade >= 80 and Grade <= 99 :
        print('小明的奖励是一台iPhone')
    elif Grade >= 60 and Grade <= 79 :
        print('小明的奖励是一本参考书')
    else :
        print('小明没有奖励')
else :
    print('你的输入不合法')