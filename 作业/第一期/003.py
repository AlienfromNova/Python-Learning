#作业003
#彩色螺旋
#根本算法：迭代
from turtle import *
bgcolor("black")
for i in range(180):
    pencolor(["red", "yellow", "green", "blue", "orange", "purple"][i%6])
    fd(i+i)
    left(61)
    width(i/30)
done()
