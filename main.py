import telebot

bot = telebot.TeleBot('6786169348:AAF2di7GowPZ8iCw8DO3GThLFVQhyNrwiCo')
import datetime


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я здесь, чтобы помочь вам. Какие у вас вопросы или задачи?',
                     parse_mode='Markdown')


@bot.message_handler(commands=['reminder'])
def main(message):
    bot.send_message(message.chat.id, 'Хотите что-то запомнить? Введите напоминание здесь.', parse_mode='Markdown')


@bot.message_handler(commands=['time'])
def main(message):
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, f'Текущее время ${now}.', parse_mode='Markdown')


import time


@bot.message_handler(commands=['search'])
def main(message):
    bot.send_message(message.chat.id, 'Поиск в интернете...', parse_mode='Markdown')
    time.sleep(2)
    bot.send_message(message.chat.id, 'Ничего не найдено :(', parse_mode='Markdown')


bot.infinity_polling()