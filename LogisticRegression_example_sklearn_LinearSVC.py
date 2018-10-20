#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import numpy as np

# X表示年龄 Y表示身高
X = [[2], [4], [6], [8], [10], [14], [16], [18]]
Y = [[60], [100], [110], [120], [140], [150], [155], [165]]

print(u'数据集X（年龄）: ', X)
print(u'数据集Y（身高）: ', Y)

# 回归训练
clf = LinearSVC(penalty='l2')  # 使用逻辑回归
# 导入数据集
clf.fit(X, Y)
# 预测结果
res = clf.predict(np.array([20]).reshape(-1, 1))[0]
print(u'预测小明的身高：%.2f' % res+" cm")

# 预测结果
X2 = [[0], [10], [14], [25]]
Y2 = clf.predict(X2)

# 绘制线性回归图形
plt.figure()
plt.title(u'(Age & Height )LinearSVC &  Predict ')  # 标题
plt.xlabel(u'Independent Variable(Age)')  # x轴坐标
plt.ylabel(u'Dependent Variable(Height)')  # y轴坐标
plt.axis([0, 20, 50, 200])  # 区间(xmin, xmax, ymin, ymax)
plt.grid(True)  # 显示网格
plt.plot(X, Y, 'k.')  # 绘制训练数据集散点图
plt.plot(X2, Y2, 'g-')  # 绘制预测数据集直线(x轴数据，y轴数据，format_string控制曲线的格式字串 format_string 由颜色字符，风格字符，和标记字符)
plt.show()
