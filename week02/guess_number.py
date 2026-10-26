# 猜数字游戏
import random
num = random.randint(1,100)
print("欢迎来到猜数字游戏~")
count = 0
while True:
    count+=1
    guess = int(input("请输入一个数字："))
    if guess == num:
        print(f"猜对了，你一共猜了{count}次")
        break
    elif guess > num:
        print("猜大了")
        continue
    elif guess < num:
        print("猜小了")
        continue
    else:
        print("请按照要求输入")
        continue
