#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from urllib import response
import bs4, requests, webbrowser

API_TOKEN = '5230995769:AAFqcAdaEGPKDS_S4Er98JoHEFuyj8NgrG4'

bot = telebot.TeleBot(API_TOKEN)
link = "https://www.amazon.it/gp/movers-and-shakers/pc"
PRE_LINK_ANNUNCIO = "https://www.amazon.it/"

response = requests.get(link)

response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')
div_annunci = soup.find('div', class_ = 'p13n-desktop-grid')
a_annunci = div_annunci.find_all('a')
link_annunci = []



for a_annuncio in a_annunci:
          link_annuncio = str(a_annuncio.get('href'))
          link_annunci.append(link_annuncio)
          @bot.message_handler(func=lambda message: True)
          def echo_message(message):
                    bot.reply_to(message,"https://www.amazon.it/", link_annuncio)

bot.infinity_polling()