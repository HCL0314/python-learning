a = int(input("请输入学生成绩：（-1退出）"))
while a!=-1:
    if a >= 90:
        print("该学生成绩等级为A")
    elif a >= 80:
        print("该学生成绩等级为B")
    elif a >=70:
        print("该学生成绩等级为C")
    elif a >= 60:
        print("该学生成绩等级为D")
    else:
        print("该学生成绩等级为E")
    a = int(input("请输入下一位学生成绩："))

