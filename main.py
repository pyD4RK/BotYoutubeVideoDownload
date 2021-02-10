import os
import time
import telebot
from pytube import YouTube


TOKEN = "<Your TOKEN here>"

bot = telebot.TeleBot(TOKEN, parse_mode="markdown")


@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.reply_to(message, '*Olá, minha função é baixar vídeos do Youtube. Você só precisa informar a url após o comando.*\n\n_Exemplo:_\n\n/YT `https://youtu.be/1A1evTUll_Y`')


@bot.message_handler(commands=['YT'])
def download(message):
    url = message.text[4:]

    video = YouTube(url).streams.get_highest_resolution().download(skip_existing=False)
    file = open(video, 'rb')

    bot.send_video(message.chat.id, file, timeout=1000)

    file.close()
    os.remove(video)


while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        telebot.logger.error(e)
        time.sleep(15)
