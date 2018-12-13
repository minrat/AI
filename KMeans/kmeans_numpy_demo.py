#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot
import numpy as np

# 随机生成 K 个质心
def SetRandomCenter(pointers, k):
    indexs = np.random.random_integers(0, len(pointers)-1, k)
    centers = []
    for index in indexs:
        centers.append(pointers[index])
    return centers

# 绘制最终的结果
def SetPointersCenters(pointers, centers):
    i = 0
    for classs in pointers:
        cs = np.zeros(4, dtype=np.int8)
        cs[i] = 1
        cs[3] = 1
        # 强制类型转换（list转为numpy中的array）
        xy = np.array(classs)
        if len(xy)>0:
            pyplot.scatter(xy[:, 0], xy[:, 1], c=cs)
        i += 1
    centers = np.array(centers)
    pyplot.scatter(centers[:, 0], centers[:, 1], c=[0, 0, 0], linewidths=20)
    pyplot.show()

# 计算两个向量的距离
def distEclud(vecX, vecY):
    #
    out_0 = np.sqrt(np.sum(np.square(vecX - vecY)))
    # 欧式距离
    out_1 = np.sqrt(np.sum(np.power(vecX - vecY, 2)))
    return out_1

# 求这一组数据坐标的平均值,也就是新的质心
def GetKMeanCenter(data):
    xMean = np.mean(data[:, 0])
    yMean = np.mean(data[:, 1])
    return [xMean, yMean]

def KMeans(pointers, centers):
    diffAllNew = 100
    diffAllOld = 0
    afterClassfy = []
    while abs(diffAllNew - diffAllOld)>1:
        # 更新diffAllOld为diffAllNEw
        diffAllOld = diffAllNew
        # 先根据质心，对所有的数据进行分类
        afterClassfy = [[] for a in range(len(centers))]
        for pointer in pointers:
            dis = []
            for center in centers:
                dis.append(distEclud(pointer, center))
            minDis = min(dis)
            i = 0
            for d in dis:
                if minDis == d:
                    break
                else:
                    i += 1
            afterClassfy[i].append(pointer)
        afterClassfy = np.array(afterClassfy)
        # 计算所有点到其中心距离的总的和
        diffAllNews = [[] for a in range(len(centers))]
        i=0
        for classs in afterClassfy:
            for center in centers:
                if len(classs) > 0:
                    diffAllNews[i] += distEclud(classs, center)
            i += 1
        diffAllNew = sum(diffAllNews)
        # 更新质心的位置
        i = 0
        for classs in afterClassfy:
            classs = np.array(classs)
            if len(classs) > 0:
                centers[i] = GetKMeanCenter(classs)
            i += 1
        SetPointersCenters(afterClassfy, centers)
    print(afterClassfy)

def GenerateRandomSample(N):
    ponters = [np.random.random_integers(0, 10, 2) for a in range(N)]
    np.save("data", ponters)
    print("产生随机样本：", ponters)


if __name__ == '__main__':
    # 样本数量
    N = 24
    # 分组类别
    K = 3
    # 产生数据
    GenerateRandomSample(N)
    # 装载数据
    pointers = np.load("data.npy")
    centers = SetRandomCenter(pointers, K)
    print("集合中点：", centers)
    KMeans(pointers, centers)
