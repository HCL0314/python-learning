# 打印九九乘法表
for i in range(1,10):
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end = '')
        j += 1
    print()