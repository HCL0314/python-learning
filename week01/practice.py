money = 5000000
name = input("请输入姓名：")
def main():
    print("----------主菜单----------")
    print(f"{name}您好，欢迎来到ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    a = int(input("请输入您的选择： "))
    return a
def search(show_header):
    if(show_header):
        print("----------余额查询----------")
    print(f"{name}您好，您的余额还剩{money}元")
def inMoney(add):
    print(f"{name}您好，您存款{add}元成功")
    global money
    money= money+add
    search(False)
def exMoney(sub):
    print(f"{name}您好，您取款{sub}元成功")
    global money
    money = money - sub
    search(False)
while True:
    ans = main()
    if ans == 1:
        search(True)
        continue
    elif ans == 2:
        add = int(input("请输入你要存入的数字"))
        inMoney(add)
    elif ans == 3:
        sub = int(input("请输入你要取出的数字"))
        exMoney(sub)
    else:
        break

