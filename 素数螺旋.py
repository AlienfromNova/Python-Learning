#第一次修改代码
#修改了循环条件减少代码量
#增加了新的条件，当i为5的倍数时可以直接略过
#不再过滤素数2
#修改了一个很严重的逻辑问题

from math import *
import turtle as t


t.pu()
t.pensize(1.5)
t.speed(10000000)
t.title('素数螺旋')
t.color('black')
N = 0
Nlim = 1
mark = 1

for i in range(1,int(10e10)):
    #打印点迹
    j=2
    N += 1
    #t.dot(3)
    #print(i)#选择是否显示素数以外的点迹
    t.fd(8)
    #依据Nmax和N的函数图像得出螺旋的代码
    if N==Nlim:
        N = 0
        if mark == 2:
            Nlim += 1
            mark = 0
        t.left(90)
        mark += 1
    if i ==2 or i == 5:
        t.color('red')
        t.dot(5)
        t.color('black')
    if i % 2 != 0 and i %10 != 5:
        #判断质数
        while j<=sqrt(i+1):     #原本为j<=i-1这里依据初等数论缩减计算量
            if i%j==0:
                break
            elif j==int(sqrt(i+1)):
                print(i)
                #标记质数
                t.color('red')
                t.dot(5)
                t.color('black')
            j += 1
