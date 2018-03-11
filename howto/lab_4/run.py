# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.comparisons import thai
chatbot = ChatBot(
    'Fah', # ชื่อแชตบ็อต
    storage_adapter='chatterbot.storage.SQLStorageAdapter', # กำหนดการจัดเก็บ ในที่นี้เลือก chatterbot.storage.SQLStorageAdapter เก็บเป็น Sqllite
    database='fah2.sqlite3', # ที่ตั้งฐานข้อมูล
    statement_comparison_function=thai
)
text=""
while True:
    text=input("Text : ")
    if text=="exit":
        break
    response = chatbot.get_response(text)
    print(response)