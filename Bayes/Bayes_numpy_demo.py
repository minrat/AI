#!/usr/bin/python
# -*- coding: UTF-8 -*-

from numpy import *
def loadDataSet():
    group = array([[3, 104], [2, 100], [1, 81], [101, 10], [99, 5], [98, 2]])
    labels = [1, 0, 1, 0, 1, 0]
    return group, labels

def createDataList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)

def dataToVec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

def train_NB(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = log(p1Num/p1Denom)
    p0Vect = log(p0Num/p0Denom)
    return p0Vect,p1Vect,pAbusive

def classify_NB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)#
    p0 = sum(vec2Classify * p0Vec) + log(1-pClass1)
    if p1 > p0:
        return 1
    else:
        return 0

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createDataList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(dataToVec(myVocabList,postinDoc))
    p0V,p1V,pAb = train_NB(trainMat,listClasses)
    # 预测
    testEntry = [1, 4]
    thisDoc = dataToVec(myVocabList,testEntry)
    print(testEntry,'is be classified as : ',classify_NB(thisDoc,p0V,p1V,pAb))

if __name__ == '__main__':
    testingNB()
