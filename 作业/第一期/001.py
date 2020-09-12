#作业0001
#温度转换
#根本算法：识别不同数据、转换不同数据
while True:
    T=input("请输入温度（带符号）：")
    if T[-1] in ["F","f"]:
        C=(eval(T[:-1])-32)/1.8
        print("转换温度为：{:.2f}C"). format(C)
    elif T[-1] in ["C","c"]:
        F=1.8*eval(T[:-1])+32
        print("转换温度为{:.2f}F"). format(F)
    else:
        print("输入格式错误")
