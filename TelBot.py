# import telebot
import mysql

# import TokenMe

from datetime import date
# from datetime import datetime
# TOKEN=TokenMe.TOKEN
# TelBot = telebot.TeleBot(TOKEN)
# from telebot import apihelper
# waktusekarang=datetime.now()
#
# class Mybot:
#     def __init__(self):
#         self.message
#
#         @TelBot.message_handler(commands=['start', 'help'])
#         def start(message):
            photo = open('img/rpl.png', 'rb')
            TelBot.send_photo(message.form_user.id, photo)
            # teks=TokenMe.help+ "\n --- admin dan developer @Firhan Nur F - SMK Taruna Bhakti---"+"\n " \
            #                         "hari ini tanggal" + str(waktusekarang)
            # TelBot.reply_to(message, teks)
# print("--- Bot Lagi Jalan ---")
# TelBot.polling(none_stop=True)