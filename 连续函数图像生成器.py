from turtle import *
from math import *

#setting
sp = 0
xlt = -40
xrt = 40
wn = Screen()
obj = Turtle()
wn.title("连续函数图像生成器V1.0")
wn.bgcolor("black")
obj.color("white")
obj.speed(0)
obj.hideturtle()

#设置速度
def sup():
    global sp
    sp += 1
    obj.speed(sp)
    print("当前速度为",obj.speed())
    if sp > 10:
        sp = 0
    wn.listen()
def sdown():
    global sp
    sp -= 1
    obj.speed(sp)
    print("当前速度为",obj.speed())
    if sp < 0:
        sp = 0
    wn.listen()

#修改x定义区间
def changex():
    global xlt
    global xrt
    xlt = eval(textinput("请输入区间左临界值","xleft="))
    xrt = eval(textinput("请输入区间右临界值","xright="))
    wn.listen()

#生成图像
def create():
    #print("成功调用")
    global xlt
    global xrt
    x = xlt
    f = textinput("输入函数","y=")
    obj.pu()
    obj.goto(10*x,10*eval(f)-100)  #坐标系放大十倍，坐标系下压(10)
    obj.pd()
    
    x += 0.25
    while x <= xrt:
        obj.goto(10*x,10*eval(f)-100)
        x += 0.25
    wn.listen()

def clean():
    obj.clear()
    wn.listen()

#interact
print("""
介绍：
按下enter键改变定义开区间
按下space键输入函数（必须是python代码下的）
按Q提升速度，按P降低速度
按T清除图像
===============================
作者：随风铃动的尛善
由于本人能力有限，存在一定的bug且暂时没能力修复
已知bug：
②一旦输入出错、不符合数学要求时需要重新启动才能继续使用
③无法判断间断点
④小范围内函数可能会出错
""")
wn.onkeypress(create,"space")
wn.onkeypress(changex,"Return")
wn.onkeypress(clean,"t")
wn.onkeypress(sup,"q")
wn.onkeypress(sdown,"p")
wn.listen()
done()
