# -*- coding: utf-8 -*-
from pythainlp import word_tokenize
from pythainlp.word_vector import thai2vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
model=thai2vec.get_model()
def sentence_vectorizer(ss,dim=300,use_mean=True):
    s = word_tokenize(ss)
    vec = np.zeros((1,dim))
    for word in s:
        if word in model.wv.index2word:
            vec+= model.wv.word_vec(word)
        else: pass
    if use_mean: vec /= len(s)
    return vec
def sentence_similarity(s1,s2):
    return cosine_similarity(sentence_vectorizer(s1),sentence_vectorizer(s2))
sentences = [
    "ผมเป็นนักศึกษา",
    "นักศึกษาคือผม",
    "ผมเป็นนักศึกษาเรียนที่มข.",
    "ผมเป็นนักศึกษามหาลัยขอนแก่น",
    "เขาเป็นชาวนา",
    "ผมเป็นนักวิทยาศาสตร์"
]
 
focus_sentence = "ผมเป็นนักศึกษามข."
 
for sentence in sentences:
    print ("Similarity(\"%s\", \"%s\") = %.3f" % (focus_sentence, sentence, sentence_similarity(focus_sentence, sentence)))