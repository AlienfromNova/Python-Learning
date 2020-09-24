#测试代码

import random as r
import time as t
class bio:
    def __init__(self,hp,atk):
        self.hp=hp
        self.atk=atk
player=bio(100,r.randint(2,12))
monster=bio(100,r.randint(2,12))
while player.hp>0 and monster.hp>0:
    player.hp-=player.atk
    print("玩家剩余生命%d"%player.hp)
    monster.hp-=monster.atk
    print("怪兽剩余生命%d"%monster.hp)
t.sleep(1)
if player.hp>0 and monster.hp<=0:
    print("胜利")
elif player.hp<=0 and monster.hp>0:
    print("失败")
else:
    print("平局")
