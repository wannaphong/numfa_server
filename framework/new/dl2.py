# -*- coding: utf-8 -*-

import os
import numpy as np
import pickle
from keras.models import Sequential
from pythainlp.word_vector import thai2vec
from keras.layers.recurrent import LSTM,SimpleRNN
from sklearn.model_selection import train_test_split

with open("db.pickle") as f:
    vec_x,vec_y=pickle.load(f)

vec_x=np.array(vec_x,dtype=np.float)
vec_y=np.array(vec_y,dtype=np.float)

x_train,x_test,y_train,y_test = train_test_split(vec_x,vec_y,test_size=0.2,random_state=1)

model = Sequential()
model.add(LSTM(output_dim=300,input_shape=x_train.shape[1:],return_sequences=True, init='glorot_normal', inner_init='glorot_normal', activation='sigmoid'))
model.add(LSTM(output_dim=300,input_shape=x_train.shape[1:],return_sequences=True, init='glorot_normal', inner_init='glorot_normal', activation='sigmoid'))
model.add(LSTM(output_dim=300,input_shape=x_train.shape[1:],return_sequences=True, init='glorot_normal', inner_init='glorot_normal', activation='sigmoid'))
model.add(LSTM(output_dim=300,input_shape=x_train.shape[1:],return_sequences=True, init='glorot_normal', inner_init='glorot_normal', activation='sigmoid'))
model.compile(loss='cosine_proximity', optimizer='adam', metrics=['accuracy'])

model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM500.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM1000.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM1500.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM2000.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM2500.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM3000.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM3500.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM4000.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM4500.h5')
model.fit(x_train, y_train, nb_epoch=500,validation_data=(x_test, y_test))
model.save('LSTM5000.h5')      
predictions=model.predict(x_test) 
mod = thai2vec.get_model()
[mod.most_similar([predictions[10][i]])[0] for i in range(15)]