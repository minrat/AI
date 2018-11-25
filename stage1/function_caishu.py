#!/bin/bash/env python
# -*- coding: utf-8

import random
def caishu():
    result = 1
    count = 0
    while result <= 3:
        target = random.randint(1, 6)
        guess = input("你猜是多少？\n")
        if str(guess) == str(target):
            print("猜对了\n")
            count += 1
        else:
            print("正确结果是："+str(target))
            print("猜错了，重新再猜一次\n")
        result += 1
    if count >= 2:
        print("恭喜你，过关了～")
    else:
        print("本次闯关失败，再接再厉哦，加油加油~~~\n")

if __name__ == '__main__':
    caishu()
