#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.tokenize import word_tokenize
import jieba.analyse

my_text_zh = "先生/小姐，大家好。今天天气很好。欢迎来到VipJr，我们一起学习人工智能，我们希望你都能获得你们想要的知识。"
my_text_en = "Hello Mr/Miss. Somebody." \
          "Today is a good day.How are you? Welcome To vipJr. All Of Us Hope That You Will Get Your Want. "
print("中文：", word_tokenize(my_text_zh))
print("英文：", word_tokenize(my_text_en))
# 第一个参数：待提取关键词的文本
# 第二个参数：返回关键词的数量，重要性从高到低排序
# 第三个参数：是否同时返回每个关键词的权重
# 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词
print("-----------------------[中文 Section]----------------------------")
keywords = jieba.analyse.extract_tags(my_text_zh, topK=6, withWeight=True, allowPOS=())
# 访问提取结果
for v, n in keywords:
    # 分别为关键词和相应的权重
    print(v, ': \t', n)
print("-----------------------[英文 Section]----------------------------")
keywords = jieba.analyse.extract_tags(my_text_en, topK=6, withWeight=True, allowPOS=())
# 访问提取结果
for v, n in keywords:
    # 分别为关键词和相应的权重
    print(v, ': \t', n)
print("-----------------------[TextRank 提取]----------------------------")
# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
print(my_text_zh)
keywords = jieba.analyse.textrank(my_text_zh, topK=6, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'), withFlag=False)
print("keywords:", keywords)
for v, n in keywords:
    # 分别为关键词和相应的权重
    print(v, ': \t', n)
