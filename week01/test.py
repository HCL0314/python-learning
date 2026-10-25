print("Hello World!")
print(666)
# 单行注释
"""多行注释
"""
money = 50
print("钱包还有",money)
# 类型
print(type(999))
a = type(333)
print(a)
# 类型转换
c = int(99.99)
print(c)
# 运算符
print("1+1=",1+1)
print("4/2=",4/2)# 结果为浮点型
print("11//2=",11//2)# 整除
print("2**2=",2**2)# **求平方，此处是2的二次方

name='hi'
name1="""nihao"""
name2="hello"
print(name1+name2+name)
# 字符串内包含引号
a = '"a"'
b = "'b'"
c = "\"c\""
print(a+b+c)

#精度控制
num = 11.75
print("%7.2f"%num)#.也要占一个宽度

# 字符串格式化
name = "hcl"
print(f"my name is {name}")

name=input("your name is...")# 默认读取字符串类型
print("ok,%s,hi"%name)

age = 30
if age >=18:
    print(f"我已经{age}岁了")
    print("hi")
print("时间过得真快")




