from sklearn.cluster import MiniBatchKMeans
import numpy as np

def createDataSet():
    group = np.array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2], [100, 100]])
    return group

# 通过KMeans进行聚合
def classify(dataSet,N):
    # 取得KMeans
    mbk = MiniBatchKMeans(init='k-means++', n_clusters=3, batch_size=10,
                          n_init=10, max_no_improvement=10, verbose=0).fit(dataSet)
    return mbk

if __name__ == '__main__':
    # 分类
    N = 3
    dataSet = createDataSet()
    kmeans = classify(dataSet,N)
    data_inject = np.array([[1, 4],[0, 0], [4, 4]])
    output = kmeans.predict(data_inject)
    print("测试数据为:", data_inject, "分类结果为：", output)
