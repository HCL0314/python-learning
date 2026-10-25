# 定义函数
def say_hi():
    print("hi~")
# 调用函数
say_hi()

# global关键字将局部变量声明成全局变量
num = 100
def test_a():
    global num
    num = 200
    print(num)
test_a()
print(num)