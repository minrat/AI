#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 引入伯努利朴素贝叶斯
from sklearn.naive_bayes import BernoulliNB
import numpy as np

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    return group, labels

# 通过BernoulliNB进行分类
def classify(dataSet, labels):
    # 取得BernoulliNB分类器
    cls = BernoulliNB()
    cls.fit(dataSet, labels)
    return cls

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    knn=classify(dataSet, labels)
    data_inject = np.array([[1, 4]])
    output = knn.predict(data_inject)
    print("测试数据为:", data_inject, "分类结果为：", output)
