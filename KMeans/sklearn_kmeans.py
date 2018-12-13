#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.cluster import KMeans
import numpy as np

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2], [100, 100]])
    return group

# 通过KMeans进行聚合
def classify(dataSet,N):
    # 取得KMeans
    kmeans = KMeans(init='k-means++', n_clusters=N, random_state=0).fit(dataSet)
    return kmeans


if __name__ == '__main__':
    # 分类
    N = 3
    dataSet = createDataSet()
    kmeans = classify(dataSet,N)
    lables = kmeans.labels_
    print(lables)
    data_inject = np.array([[1, 4],[0, 0], [4, 4]])
    output = kmeans.predict(data_inject)
    out = kmeans.cluster_centers_
    print("测试数据为:", data_inject, "分类结果为：", output)
