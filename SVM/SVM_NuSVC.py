#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sklearn.svm import NuSVC
import numpy as np

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    return group, labels

# 通过NuSVC进行分类
def classify(dataSet, labels):
    # 取得NuSVC分类器
    cls = NuSVC()
    cls.fit(dataSet, labels)
    return cls

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    knn=classify(dataSet, labels)
    data_inject = np.array([[1, 4]])
    output = knn.predict(data_inject)
    print("测试数据为:", data_inject, "分类结果为：", output)
