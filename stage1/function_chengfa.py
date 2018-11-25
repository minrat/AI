#!/bin/bash/env python
# -*- coding: utf-8

# 乘法表

def chengfa(N):
    for i in range(1, N+1):
        result = ""
        for j in range(1, i + 1):
            result +="%d x %d=%d  " % (j, i, i * j)
        print(result)


if __name__ == '__main__':
    N = input("Your Want Number Is?\n")
    chengfa(int(N))
