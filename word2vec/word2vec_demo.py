# -*- coding:UTF-8 -*-
from gensim.models import word2vec
import gensim
import logging
import jieba
import os


# 处理训练模型的语料
def create_data_set(src_file):
    global dest_file
    dest_file = src_file + '_jieba_out'

    # 文件读取
    f1 = open(src_file, 'r', encoding='utf-8')
    text = f1.read()

    # 采用精确模式
    new_text = jieba.cut(text, cut_all=False)
    str_out = ' '.join(new_text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('‘', '').replace('’', '').replace('、', '').replace('-', '').replace('「', '')\
        .replace('」', '').replace('~', '')

    # 文件写入
    f2 = open(dest_file, 'w', encoding='utf-8')
    f2.write(str_out)


# model_file_name为训练语料,save_model为模型名
def model_train(train_file_name, out_model_file):
    # 模型训练，生成词向量
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # 加载语料
    sentences = word2vec.Text8Corpus(train_file_name)

    # 训练skip-gram模型; 默认window=5
    model = gensim.models.Word2Vec(sentences, size=200)
    model.save(out_model_file)

    # 以二进制类型保存模型
    model.wv.save_word2vec_format(out_model_file + ".bin", binary=True)


if __name__ == '__main__':
    # 测试数据（源文件）
    src_file = 'demo_data.txt'
    if not os.path.exists(src_file):
        print(src_file+"Not Exist , Please Double Check.")
    else:
        # 加载
        create_data_set(src_file)

        # 判断模型文件是否存在
        export_model = dest_file + '.model'
        if not os.path.exists(export_model):
            model_train(dest_file, export_model)
        else:
            print('模型 ['+export_model+'] 已存在，跳过...')

        # 加载已训练好的模型
        trained_model = word2vec.Word2Vec.load(export_model)

        # 计算两个词的相似度/相关程度
        relate_value = trained_model.similarity("盆菜", "牛肉")
        print(u" [盆菜] 和 [牛肉] 的相似度为：", relate_value)

        # 计算与指定词的相关词（top）列表
        y2 = trained_model.most_similar("牛肉", topn=10)
        print(u"与 [牛肉] 最相关的词有：\n")
        for item in y2:
            print(item[0], item[1])
