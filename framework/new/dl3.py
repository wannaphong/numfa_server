# -*- coding: utf-8 -*-
import os
from scipy import spatial
import numpy as np
from pythainlp.word_vector import thai2vec
import pythainlp
from keras.models import load_model


model=load_model('LSTM5000.h5')
mod = thai2vec.get_model()
while(True):
    x=input("Enter the message : ")
    sentend=np.ones((300,),dtype=np.float64) 

    sent=pythainlp.word_tokenize(x.lower())
    sentvec = [mod[w] for w in sent if w in mod.vocab]

    sentvec[14:]=[]
    sentvec.append(sentend)
    if len(sentvec)<15:
        for i in range(15-len(sentvec)):
            sentvec.append(sentend) 
    sentvec=np.array([sentvec])
    
    predictions = model.predict(sentvec)
    outputlist=[mod.most_similar([predictions[0][i]])[0][0] for i in range(15)]
    output=' '.join(outputlist)
    print (output)