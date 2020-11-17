from math import *
import turtle as t


i = 1
t.pu()
t.pensize(1.5)
t.speed(10000000)
t.title('素数螺旋')
t.color('black')
N = 0
Nlim = 1
mark = 1

while True:
    #打印点迹
    j=2
    N += 1
    #t.dot(3)#选择是否显示素数以外的点迹
    t.fd(8)
    #依据Nmax和N的函数图像得出螺旋的代码
    if N==Nlim:
        N = 0
        if mark == 2:
            Nlim += 1
            mark = 0
        t.left(90)
        mark += 1
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
    i+=2 #过滤偶数
