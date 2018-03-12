# -*- coding: utf-8 -*-
import telebot
import time
#from telepot.loop import MessageLoop

bot = telebot.AsyncTeleBot('507188636:AAErli3ZBt­iT0ZB-3Ch4MHOtjIRLOU­EiffU')
time.sleep(4)
#bot.getMe()
"""def handle(msg):
    bot.sendMessage(msg['chat']['id'].encode('utf8'),msg['text'].encode('utf8'))

MessageLoop(bot, handle).run_as_thread()

print ('I am listening ...')
input()"""
task = bot.get_me() # Execute an API call
# Do some other operations...
a = 0
for a in range(100):
	a += 10

result = task.wait() 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
print ('I am listening ...')
bot.polling()
