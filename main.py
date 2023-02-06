import telebot
from telebot import types
import config
import pyautogui as pg
import os
import random
import cv2
import numpy

bot = telebot.TeleBot('6044419328:AAEJndexkKWVm-wgAKMjRs2YqUbOlZpi7yo')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здраствуйте, {message.from_user.first_name} {message.from_user.last_name}'
    sticker = '👋'
    markup = types.ReplyKeyboardMarkup()
    screenshot = types.KeyboardButton('/screenshot')
    youtube = types.KeyboardButton('/youtube')
    start = types.KeyboardButton('/start')
    music = types.KeyboardButton('/music')
    code = types.KeyboardButton('/code')
    powerOff = types.KeyboardButton('/shutdown')
    restart = types.KeyboardButton('/restart')
    camera = types.KeyboardButton('/you_see_me?')

    markup.add(screenshot, start, youtube, music, code, powerOff, restart, camera)
    bot.send_message(message.chat.id, text=(sticker and mess), reply_markup=markup)

@bot.message_handler(commands=['screenshot'])
def screenshot(message):
    screenshot = pg.screenshot()
    screenshot.save('screenshot.png')
    photo = open('screenshot.png', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['youtube'])
def youtube(message):
    os.system('start https://www.youtube.com')

@bot.message_handler(commands=['music'])
def music(message):
    os.system('music.mp3')
    music = open('music.mp3', 'rb')
    bot.send_audio(message.chat.id, music)

    music_button = types.InlineKeyboardMarkup()
    music_button.add(types.InlineKeyboardButton('жми', url="https://oak08.dlmate43.xyz/?file=M3R4SUNiN3JsOHJ6WWQ2a3NQS1Y5ZGlxVlZIOCtyZ0RpdEEveVZzSEFMSUg3ZDkrbk1PMUxkb0VBYUVKeEltckVOSWYyQ3ZMZU5QQUJnYU5zNWRvVDJQU3NkQTB0VHJ3NDQ4MFVaUTBCRERobFBPM2d6Tnp6RlhUYzhpZVVPcHdhVElwaFZreDNpZUh5Yi9YdGhpei9qYXF0VWlHWWhzT3N5STBiNlR2OW9wR3hsYkVhZkh0MEprRW9SbVM5NGxBMmMrTHZRWHp6STBzNkl4OFZVMTRWNGhxamRUNHo2T0tvRjhKaVlzWnprU3ByTC8zVU1sZ1MvWElLbWNtZURFQTgrcXlDVWxKbDNOSXFDcXQ0UEloN0RsUGRhd283RzdscXFZPQ=="))
    bot.send_message(message.chat.id, 'больше музыки', reply_markup=music_button)

@bot.message_handler(commands=['code'])
def code(message):
    os.system('code')

@bot.message_handler(commands=['shutdown'])
def shutdown(message):
    os.system('shutdown /s /t 0')

@bot.message_handler(commands=['restart'])
def restart(message):
    os.system('shutdown /r /t 0')

@bot.message_handler(commands=['you_see_me?'])
def photo(message):
    os.system('photo.py')
    see = open('photo.png', 'rb')
    bot.send_photo(message.chat.id, see)

bot.polling(none_stop=True)