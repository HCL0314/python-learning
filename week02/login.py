# 简单登录验证
name = 'hcl'
password = "123456"
i = 0
flag = 0
while i != 3:
    in_name = input("请输入用户名：")
    in_password = input("请输入用户密码：")
    if in_password == password and in_name==name:
        print("登陆成功~")
        flag = 1
        break
    else:
        print("输入错误，请重新输入")
        i+=1
if flag == 0:
    print("输入错误超过三次，强制退出...")

