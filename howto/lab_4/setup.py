# -*- coding: utf-8 -*-
import db_chat_log
import pip
list_pip=["pythainlp","flask-socketio","gensim","numpy","chatterbot","scikit-learn"]
for data in list_pip:
	pip.main(['install',data])
print("pip install : OK")
db_chat_log.setup()
print("db chatlog : OK")