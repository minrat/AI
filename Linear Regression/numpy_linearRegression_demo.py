#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

class LinearRegression():
    def __init__(self):
        self.w = None

    # 训练集的拟合
    def fit(self, X, y):
        # 增加一个维度
        X = np.insert(X, 0, 1, axis=1)
        print(X.shape)
        # 公式求解
        X_ = np.linalg.inv(X.T.dot(X))
        self.w = X_.dot(X.T).dot(y)

    # 测试集的测试反馈
    def predict(self, X):
        # Insert constant ones for bias weights
        X = np.insert(X, 0, 1, axis=1)
        y_pred = X.dot(self.w)
        return y_pred

def mean_squared_error(y_true, y_pred):
    # 真实数据与预测数据之间的差值（平方平均）
    mse = np.mean(np.power(y_true - y_pred, 2))
    return mse

def create_data_set():
    X = [[2], [4], [6], [8], [10], [14], [16], [18]]
    Y = [[60], [100], [110], [120], [140], [150], [155], [165]]
    return X, Y

def main():
    # 导入数据
    data, lable = create_data_set()
    # 使用线性回归
    clf = LinearRegression()
    # 数据加载训练
    clf.fit(data, lable)
    # 测试数据
    target = [[0], [10], [14], [25]]
    # 数据预测
    y_pred = clf.predict(target)
    # 预测结果输出
    print("预测结果是：", y_pred)
    # 第四步：测试误差计算（需要引入一个函数）
    print("Mean Squared Error:", mean_squared_error(target, y_pred))
    # 绘制线性回归图形
    plt.figure()
    # 图形标题
    plt.title(u'(Age & Height )LinearRegression &  Predict ')
    # x标题
    plt.xlabel(u'Independent Variable(Age)')
    # y轴标题
    plt.ylabel(u'Dependent Variable(Height)')
    # 显示网格
    plt.grid(True)
    # 可视化输出
    plt.scatter(data, lable,  color='black')
    # 原始结果输出
    plt.plot(data, lable, color='red', linewidth=2)
    # 预测输出
    plt.plot(target,y_pred, color='blue', linewidth=2)
    # 图形显示
    plt.show()


if __name__ == '__main__':
    main()
