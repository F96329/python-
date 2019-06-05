print('='*20,'欢迎来到唐僧大战白骨精','='*20)
print('请选择你的身份：')
print('\t1、唐僧')
print('\t2、白骨精')
player = input('请选择【1-2】')
print('='*66)
if player == '1':
    print('你选择了唐僧，将以 ->唐僧<- 的身份进行游戏')
elif player == '2':
    print('你竟然选择了白骨精。真不要脸，系统将自动为你分配角色进行游戏')
else :
    print('你的输入不合法，系统将自动为你分配角色进行游戏。')
print('='*66)
player_age = 2   #玩家生命值
player_fuck = 2   #玩家攻击力
boss_age = 10 #boss的生命值
boss_fuck = 10
print('你已经选择了唐僧，你的生命值是:',player_age,'攻击力是',player_fuck)
print('='*66)
while True:
    print('请选择你要进行的操作：')
    print('\t1、练级')
    print('\t2、打BOSS')
    print('\t3、逃跑')
    play = input('请选择【1-3】')
#处理用户选择
    if play == '1':
        player_age += 2
        player_fuck += 2
        print('你已经成功升级，现在你的生命值是:',player_age,'攻击力是',player_fuck)
    if play == '2':
        if player_fuck > boss_age:
            print('恭喜你打败了白骨精，赢得了胜利')
            break
        elif player_fuck < boss_age:
            print('不自量力，你被白骨精暴打，游戏失败')
            break
        elif player_fuck == boss_age:
            if player_age < boss_age:
                print('你两旗鼓相当，但是他血厚，你被吊打，游戏失败')
            elif player_age > boss_age:
                print('你两旗鼓相当，但是你的生命力顽强，险胜，赢得了胜利')
    elif play == '3':
        print('你个懦夫，游戏结束')
        break
    else :
        print('你的输入不合法请重新输入')



    


