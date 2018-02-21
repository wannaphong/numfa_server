# -*- coding: utf-8 -*-
from chatterbot import ChatBot
bot = ChatBot(
    'numfa',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation"
    ],
    database='database.sqlite3'
) # read_only = True ให้หยุด train