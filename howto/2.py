# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Charlie', # ชื่อแชตบ็อต
    storage_adapter='chatterbot.storage.SQLStorageAdapter', # กำหนดการจัดเก็บ ในที่นี้เลือก chatterbot.storage.SQLStorageAdapter เก็บเป็น Sqllite
    database='Charlie.sqlite3' # ที่ตั้งฐานข้อมูล
)
chatbot.set_trainer(ChatterBotCorpusTrainer) # กำหนดให้ Train จากชุดข้อมูลของ Chatterbot

chatbot.train(
    "chatterbot.corpus.english"
) # เรียกใช้ชุดข้อมูล chatterbot.corpus.english
text=""
while True:
    text=input("Text : ")
    if text=="exit":
        break
    response = chatbot.get_response(text)
    print(response)