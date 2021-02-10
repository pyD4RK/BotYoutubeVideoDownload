import requests
import telebot
from telebot import types


TOKEN = "<your token here>"

bot = telebot.TeleBot(TOKEN=TOKEN, parse_mode="markdown")