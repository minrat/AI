#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy import *

# 给出训练数据以及对应的类别
def createDataSet():
    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    return group, labels

# 通过KNN进行分类
def classify(input, dataSet, label, k):
    dataSize = dataSet.shape[0]
    # 计算欧式距离
    diff = tile(input, (dataSize, 1)) - dataSet
    sqdiff = diff ** 2
    # 行向量分别相加，从而得到新的一个行向量
    squareDist = sum(sqdiff, axis=1)
    dist = squareDist ** 0.5

    # 对距离进行排序
    # 根据元素的值从大到小对元素进行排序，返回下标
    sortedDistIndex = argsort(dist)

    classCount = {}
    for i in range(k):
        voteLabel = label[sortedDistIndex[i]]
        # 对选取的K个样本所属的类别个数进行统计
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    # 选取出现的类别次数最多的类别
    maxCount = 0
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            classes = key
    return classes

if __name__ == '__main__':
    dataSet, labels = createDataSet()
    data_inject = array([1, 4])
    K = 3
    output = classify(data_inject, dataSet, labels, K)
    print("测试数据为:", data_inject, "分类结果为：", output)
