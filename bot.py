import telebot
import os 
import django
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()
from telebot import types
from main.models import Callback



bot = telebot.TeleBot(token=TOKEN)

my_chat_id = 657061394
all_buttons = ['All callbacks 🧐']

name = 'Nurbek'

@bot.message_handler(commands=['start'])
def start(message):
    global my_chat_id, all_buttons

    admin = False 
    response = ''
    if message.chat.id == my_chat_id:
        admin = True
    if admin:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        all_callbacks = types.KeyboardButton('All callbacks 🧐')
        markup.add(all_callbacks)
        response = f'Hi there Nurbek. Happy to see you here again, how are you?'
        bot.send_message(message.chat.id, response, reply_markup=markup)
    else:
        response = f'Hi there. My name is {name}. \n\nAs an experienced backend Python developer, I am skilled in developing and maintaining robust, scalable, and high-performance server-side applications. With a strong understanding of databases, APIs, and web frameworks, I am well-versed in designing and implementing complex systems that meet the needs of modern web applications. \n\nIs there anything i can help u with?'
        bot.send_message(message.chat.id, response)



@bot.message_handler(content_types=['text'])
def text_handler(message):
    global all_buttons
    admin = False 
    response = ''
    if message.chat.id == my_chat_id:
        admin = True
    response = ''
    if message.text == all_buttons[0] and admin:
        callbacks = Callback.objects.all()
        if len(callbacks) != 0:
            for i in callbacks:

                response += f'''
Callback #{i.id}

email: {i.email}
topic: {i.topic}
text: {i.text}
-----------------------
            
    '''
        else:
            response = f'No callbacks yet'
    else: 
        response = 'Sorry, seems you are not Nurbek :)'
    

    bot.send_message(message.chat.id, response)



bot.infinity_polling()
