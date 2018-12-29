#!/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

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
        # h(theta)=theta.T.dot(X)
        # Insert constant ones for bias weights
        X = np.insert(X, 0, 1, axis=1)
        y_pred = X.dot(self.w)
        return y_pred

def mean_squared_error(y_true, y_pred):
    # 真实数据与预测数据之间的差值（平方平均）
    mse = np.mean(np.power(y_true - y_pred, 2))
    return mse

def createDataSet():
    X = [[2], [4], [6], [8], [10], [14], [16], [18]]
    Y = [[60], [100], [110], [120], [140], [150], [155], [165]]
    return X, Y

def main():
    # 第一步：导入数据
    # Load the diabetes dataset
    diabetes = datasets.load_diabetes()

    # Use only one feature
    X = diabetes.data[:, np.newaxis, 2]
    print(X.shape)

    # 第二步：将数据分为训练集以及测试集
    # Split the data into training/testing sets
    x_train, x_test = X[:-20], X[-20:]

    # Split the targets into training/testing sets
    y_train, y_test = diabetes.target[:-20], diabetes.target[-20:]

    # 第三步：导入线性回归类（之前定义的）
    clf = LinearRegression()
    # 训练
    clf.fit(x_train, y_train)
    # 测试
    y_pred = clf.predict(x_test)

    # 第四步：测试误差计算（需要引入一个函数）
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

    # matplotlib 可视化输出
    # Plot the results
    # 散点输出
    plt.scatter(x_test[:,0], y_test,  color='black')

    # 预测输出
    plt.plot(x_test[:,0], y_pred, color='blue', linewidth=3)
    plt.show()


if __name__ == '__main__':
    main()
