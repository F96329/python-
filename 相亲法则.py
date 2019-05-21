        # 大家都知道，男大当婚，女大当嫁。那么女方家长要嫁女儿，当然要提出一定的条件：
        #     高：180cm以上; 富:1000万以上; 帅:500以上;
        #     如果这三个条件同时满足，则:'我一定要嫁给他'
        #     如果三个条件有为真的情况，则:'嫁吧，比上不足，比下有余。'
        #     如果三个条件都不满足，则:'不嫁！'
height = float(input('请输入你的身高(厘米)：'))
money = float(input('请输入你的存款（万）：'))
handsome = float(input('请输入你的帅（帅气值）：'))
if height > 180 and money > 1000 and handsome > 500 :
    print('我一定要嫁给他')
elif height > 180 or money > 1000 or handsome > 500 :
    print('嫁吧，比上不足，比下有余')
else :
    print('不嫁')
