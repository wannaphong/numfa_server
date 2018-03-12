# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from pythainlp.tokenize import word_tokenize
from chatterbot.trainers import ListTrainer
from thai import thai
import codecs,json
with codecs.open("data.json", 'r',encoding='utf8') as f:
    data=json.load(f)
cor=data["conversations"]
chatbot = ChatBot(
    'Fah', # ชื่อแชตบ็อต
    storage_adapter='chatterbot.storage.SQLStorageAdapter', # กำหนดการจัดเก็บ ในที่นี้เลือก chatterbot.storage.SQLStorageAdapter เก็บเป็น Sqllite
    database='fah2.sqlite3', # ที่ตั้งฐานข้อมูล
    statement_comparison_function=thai
)
chatbot.set_trainer(ListTrainer)
for data_list in cor:
    chatbot.train(data_list)
text=""
while True:
    text=input("Text : ")
    if text=="exit":
        break
    response = chatbot.get_response(text)
    print(response)
