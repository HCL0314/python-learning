# 输入多门课程成绩
# 输出平均分、最高分、最低分和等级
print("请依次输入语数外物化生成绩：")
i = 0
sum = 0
max_grade = 0
min_grade = 101
while i < 6:
    subject = int(input())
    if max_grade < subject:
        max_grade = subject
    sum+=subject
    if min_grade > subject:
        min_grade = subject
    i+=1

average = float(sum / 6)
if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif average > 70:
    grade = "C"
else:
    grade = "D"
print("你的平均分是%.2f,最高分是%d,最低分是%d，等级是%s"%(average,max_grade,min_grade,grade))