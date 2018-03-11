# -*- coding: utf-8 -*-
import telepot
import time
from telepot.loop import MessageLoop

bot = telepot.Bot('507188636:AAErli3ZBt­iT0ZB-3Ch4MHOtjIRLOU­EiffU')
time.sleep(4)
#bot.getMe()
def handle(msg):
    bot.sendMessage(msg['chat']['id'].encode('utf8'),msg['text'].encode('utf8'))

MessageLoop(bot, handle).run_as_thread()

print ('I am listening ...')
input()
