# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie', # ชื่อแชตบ็อต
    trainer='chatterbot.trainers.ListTrainer' # เลือกให้ Train จาก List
)
chatbot.train([
    "Hi there!",
    "Hello",
])

chatbot.train([
    "Greetings!",
    "Hello",
])
chatbot.train([
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "You are welcome.",
])

# Get a response to the input text 'How are you?'
text=""
while True:
    text=input("Text : ")
    if text=="exit":
        break
    response = chatbot.get_response(text)
    print(response)