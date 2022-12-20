from random import randint
import time,sys
from os import system
import time
# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount
        

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName == '鹰妖':
            self.strength -= 20
            print (self.strength)
        elif monster.typeName == '狼妖':
            self.strength -= 80
            print (self.strength)
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
            print (self.strength)
        elif monster.typeName== '狼妖':
            self.strength -= 20
            print (self.strength)
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****

***************************************

'''
)


# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '


#定时显示信息
def temp_print(val: str):
    print(val)
    time.sleep(1)
    system('cls')

# 显示 10s妖怪信息
temp_print('以下内容将在10s后消失！ '+notification)
print ('现在你有1000灵石，请根据你记忆的妖怪种类和数量，选择雇佣多少个弓箭兵和斧头兵')
print('   弓箭兵：雇佣价： 100 灵石 最大生命值： 100')
print('   斧头兵：雇佣价： 120 灵石 最大生命值： 120')


#生成士兵
a=int(input('我需要弓箭兵：'))

archersList = list()
axemenList = list()
stoneNumber = 1000
while stoneNumber>100
    for n in range (a) :
        nickname = input('第'+str(n+1)+'个弓箭兵，名字是')
        archersList.append(Archer(nickname))

b=int(input('我需要斧头兵：'))
for n in range (b) :
    nickname = input('第'+str(n+1)+'个斧头兵，名字是')
    axemenList.append(Axeman(nickname))

#显示士兵信息
print ('你雇佣的士兵如下：')
for i in range(int(a)):
    print(archersList[i].name+archersList[i].typeName)
for i in range (int(b)):
    print(axemenList[i].name+axemenList[i].typeName)
stoneNumber = 1000-(100*a+120*b)
Player(stoneNumber)
print ('您还剩余的灵石为：'+str(stoneNumber))

for i in range(7):
    print('即将进入第'+str(i+1)+'座森林，请跟据你记忆的妖怪派出一名战士')
    c = input ('选择弓箭兵（1）or斧头兵（2）')
    if c == '1':
        x = int(input('选择(从0开始)'))
        if x<int(a+b):
            print('派出'+archersList[x].name)
        else:
            print ('只有'+(a+b)+'名！')
        print (forestList[i].monster.typeName+'出现！')
        print ('搏斗中....')
        Archer(archersList[x].name).fightWithMonster(forestList[i].monster)
        
        h = input('是否补养？y or n')
        while h == 'y':
            stoneCount = input('恢复多少生命值？：')
            Archer(archersList[x].name).healing(stoneCount)
            stoneNumber -=int(stoneCount)
            while stoneNumber<0:
                print('灵石不足！')
                break
            print ('您还剩余的灵石为：'+str(stoneNumber))
            break
    else :
        x = int(input('选择(从0开始)'))
        if x<int(a+b):
            print('派出'+axemenList[x].name)
        else:
            print ('只有'+(a+b)+'名！')
        print (forestList[i].monster.typeName+'出现！')
        print ('搏斗中....')
        Axeman(axemenList[x].name).fightWithMonster(forestList[i].monster)
    
        h = input('是否补养？y or n')
        while h == 'y':
            stoneCount = input('恢复多少生命值？：')
            Axeman(axemenList[x].name).healing(stoneCount)
            stoneNumber -=int(stoneCount)
            while stoneNumber<0:
                print('灵石不足！')
                break
            print ('您还剩余的灵石为：'+str(stoneNumber))
            break
