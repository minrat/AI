# 主题： 99乘法


# 复习：% {}.format（） 显示

# 注意{}，不带序号的时候，前后按照顺序自动匹配


# 注意{}的前后格式：带序号注意不要超过范围（从0开始），不写序号，自动前后按序一一匹配

# method-01
for i in range(1, 10):
    for j in range(1, i):
        print("{}x{}={}\t".format(i, j, i*j), end='')
    print()

# method-02
abc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in abc:
    j = 1
    while j <= i:
        print("{}x{}={}\t".format(i, j, i * j), end='')
        j += 1
    print()

# 注意： % 的前后格式需要一一匹配，    
# method-03
for i in range(1, 10):
    result = ""
    for j in range(1, i + 1):
        result += "%d x %d = %d	" % (j, i, i * j)
    print(result)
