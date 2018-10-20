#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
# X:年龄，Y:身高 数据集
X = [2, 4, 6, 8, 10, 14, 16, 18]
Y = [60, 100, 110, 120, 140, 150, 155, 165]
# 多项式系数，（多项式拟合相当于线性拟合）
N = 1
# 拟合点集X得到n级多项式，其中x为横轴长度，返回多项式的系数
coefficient = np.polyfit(X, Y, N)
print(coefficient)
# 获取表达式
expression = np.poly1d(coefficient)
print("Height(x)= "+str(expression))
