# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from thai import thai
chatbot = ChatBot(
    'Fah', # ชื่อแชตบ็อต
    storage_adapter='chatterbot.storage.SQLStorageAdapter', # กำหนดการจัดเก็บ ในที่นี้เลือก chatterbot.storage.SQLStorageAdapter เก็บเป็น Sqllite
    database='fah2.sqlite3', # ที่ตั้งฐานข้อมูล
    statement_comparison_function=thai,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'timenow.TimeLogicAdapter',
        {
            'import_path':'chatterbot.logic.LowConfidenceAdapter',
            'threshold':0.65,
            'default_response': 'ขออภัยค่ะ ฉันไม่เข้าใจสิ่งที่คุณต้องการบอกฉันค่ะ'
        }
    ]
)
text=""
while True:
    text=input("Text : ")
    if text=="exit":
        break
    response = chatbot.get_response(text)
    print(response)