# -*- coding: utf-8 -*-

import os
import json
import pythainlp
import codecs
import numpy as np
import pickle
from gensim import corpora,models,similarities
from pythainlp.word_vector import thai2vec
model=thai2vec.get_model()
with codecs.open("data.json", 'r',encoding='utf8') as f:
    data=json.load(f)
cor=data["conversations"]

x=[]
y=[]

path2="corpus"

for i in range(len(cor)):
    for j in range(len(cor[i])):
        if j<len(cor[i])-1:
            x.append(cor[i][j])
            y.append(cor[i][j+1])

tok_x=[]
tok_y=[]
for i in range(len(x)):
    tok_x.append(pythainlp.word_tokenize(x[i].lower()))
    tok_y.append(pythainlp.word_tokenize(y[i].lower()))

#sentend=np.ones((300L,),dtype=np.float32)

vec_x=[]
for sent in tok_x:
    sentvec=[model[w] for w in sent if w in model.vocab]
    vec_x.append(sentvec)

vec_y=[]
for sent in tok_y:
    sentvec=[model[w] for w in sent if w in model.vocab]
    vec_y.append(sentvec)

with open("db.pickle"."w") as f:
    pickle.dump([vec_x,vec_y],f)