#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn import linear_model

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    return group, labels

# 通过KNN进行分类
def classify(dataSet, labels):
    cls = linear_model.LogisticRegression(penalty='l2')
    cls.fit(dataSet, labels)
    return cls

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    cls=classify(dataSet, labels)
    data_inject = np.array([[1, 4]])
    output = cls.predict(data_inject)
    print("测试数据为:", data_inject, "分类结果为：", output)
