#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class LogisticRegression(object):
    @staticmethod
    def sigmoid(x):
        return 1.0/(1 + np.exp(-x))

    def gradient_ascent(self, dataset, labels, max_iter=10000):
        dataset = np.matrix(dataset)
        vlabels = np.matrix(labels).reshape(-1, 1)
        m, n = dataset.shape
        w = np.ones((n, 1))
        alpha = 0.001
        ws = []
        for i in range(max_iter):
            error = vlabels - self.sigmoid(dataset*w)
            w += alpha*dataset.T*error
            ws.append(w.reshape(1, -1).tolist()[0])
        self.w = w
        return w, np.array(ws)

    def classify(self, data, w=None):
        if w is None:
            w = self.w
        data = np.matrix(data)
        prob = self.sigmoid((data*w).tolist()[0][0])
        return round(prob)

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    label = [0, 1, 1, 0, 1, 0]
    return group, label

if '__main__' == __name__:
    clf = LogisticRegression()
    dataset, labels = createDataSet()
    # 注入数据，进行模型训练
    lr = clf.gradient_ascent(dataset, labels, max_iter=50000)
    # 键入测试数据
    data_inject = np.array([[1, 4]])
    # 数据预测
    output=clf.classify(data_inject)
    print("测试数据为:", data_inject, "分类结果为：", output)


#运行结果：测试数据为: [[1 4]] 分类结果为： 1.0
