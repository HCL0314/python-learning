# 菜单式计算器
while True:
    print("===计算器===")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("0.退出")
    num = int(input("请输入你想实现的功能："))
    if num == 0:
        break
    if num < 0 or num > 4:
        print("输入的数字无效，请重新输入！")
        continue
    print("请依次输入两个数字：")
    a = float(input())
    b = float(input())
    if num == 1:
        print(f"{a}+{b}={a+b}")
    elif num == 2:
        print(f"{a}-{b}={a-b}")
    elif num == 3:
        print(f"{a}*{b}={a*b}")
    elif num == 4:
        if b == 0.0:
            print("0不能做除数")
        else:
            print(f"{a}/{b}={a/b}")
