#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import neighbors

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    return group, labels

# 通过KNN进行分类
def classify(dataSet, labels):
    # 取得knn分类器
    knn = neighbors.RadiusNeighborsClassifier(radius=100.0)
    knn.fit(dataSet, labels)
    return knn

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    knn=classify(dataSet, labels)
    data_inject = np.array([[1, 4]])
    output = knn.predict(data_inject)
    print("测试数据为:", data_inject, "分类结果为：", output)
