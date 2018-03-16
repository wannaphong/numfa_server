# -*- coding: utf-8 -*-
from flask import Flask, render_template,request, jsonify
from run import get_chatbot

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'

@app.route('/')
def index():
    return render_template('index.html')

"""@app.route('/chat')
def chat():
    return render_template('chat.html')
"""
"""@app.route('/api/chat_message', methods=['POST'])
def add_message():
    content = request.json
    data=get_chatbot(content['text'])
    return jsonify({"text":data})
"""

@app.route('/api/chat_message')
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_chatbot(userText))

if __name__ == '__main__':
    app.run()