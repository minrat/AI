# -*- coding:UTF-8 -*-
import gensim
import jieba
from gensim.models.doc2vec import Doc2Vec


TaggededDocument = gensim.models.doc2vec.TaggedDocument


# 构建基础数据
def create_data_set():
    with open("trip_02", 'r', encoding='UTF-8') as doc:
        docs = doc.readlines()
    train_docs = []
    for i, text in enumerate(docs):
        word_list = text.split(' ')
        length = len(word_list)
        word_list[length - 1] = word_list[length - 1].strip()
        document = TaggededDocument(word_list, tags=[i])
        train_docs.append(document)
    return train_docs


# 基于数据，得出决策模型
def model_train(src_data, size=200):
    model_out = Doc2Vec(src_data, min_count=1, window=3, size=size, sample=1e-3, negative=5, workers=4)
    model_out.train(src_data, total_examples=model_out.corpus_count, epochs=70)
    model_out.save('model_doc2vec_out')
    return model_out


# 基于模型，预测结果
def model_predict():
    model = Doc2Vec.load("model_doc2vec_out")
    text_test = u'春节，我们一般去云南大理游玩，游览沙溪古镇。'
    # 使用 jieba 精确模式
    text_cut = jieba.cut(text_test)
    text_raw = []
    for i in list(text_cut):
        text_raw.append(i)
    inferred_vector = model.infer_vector(text_raw)
    similar_results = model.docvecs.most_similar([inferred_vector], topn=10)
    return similar_results


if __name__ == '__main__':
    data_set = create_data_set()
    model_dm = model_train(data_set)
    similar_results = model_predict()
    for count, similar_result in similar_results:
        sentence = data_set[count]
        words = ''
        for word in sentence[0]:
            words = words + word + ' '
        print(words, similar_result)
