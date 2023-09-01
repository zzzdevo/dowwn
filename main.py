import telebot
import requests
from telebot import types,TeleBot

TOK_BOT = ("5853600134:AAEBZF6ZgSrpjYT2XnJKRwyLtt-EOtRV43Q")#token
p = "@MGIMT"
o = "@IQ7amo"
sh_btn = types.InlineKeyboardButton(text='داگرتنی ڤیدیۆ', callback_data='s1')
version = types.InlineKeyboardButton(text='Version 1.1', callback_data='v')
dev = types.InlineKeyboardButton(text='کەناڵی بۆتەکان 🧑🏻‍💻🖤', url='t.me/MGIMT')

bot = telebot.TeleBot(TOK_BOT)
@bot.message_handler(commands=["pin"], chat_types=["private"])
def weclome(message):
    v = types.InlineKeyboardMarkup()
    v.row_width = 2
    v.add(sh_btn, version, dev)

    FIRST_NAME = message.from_user.first_name
    bot.send_message(message.chat.id, f'''
	*بەخێربێی ئەزیزم {FIRST_NAME}
 دەتوانی لە ڕێگایی دوگمە ڤیدیۆی پینترێست دابگریت*''', parse_mode='markdown', reply_markup=v)


@bot.callback_query_handler(func=lambda call: True)
def sh(call):
    if call.data == 's1':
        bot.send_message(call.message.chat.id, f"*ئێستا لینکی ڤیدیۆ بنێرە*", parse_mode="markdown")

    @bot.message_handler(func=lambda m: True)
    def Url(message):
        bot.send_message(message.chat.id, f"<strong>دادەبەزێت کەمێك چاوەڕێبە . . . ❗️</strong>", parse_mode="html")
        msg = message.text
        key_1 = requests.get(f'https://dev-broksuper.pantheonsite.io/api/pin.php?url={msg}').json()["UrlVideo"]
        bot.send_message(message.chat.id, text=f'''
		مبرمج الملف : {o}
     & قناة المبرمج : {p}''', parse_mode="MarkdownV2")
        try:
            if key_1 == False:
                bot.send_message(message.chat.id, f'- الرابط خطا عزيزي')
            else:
                share_telegram = types.InlineKeyboardButton(text='گۆڕینی بۆ دەنگ',
                                                            url='https://t.me/IQCVBOT?url=' + key_1)
                s = types.InlineKeyboardMarkup()
                s.row_width = 1
                s.add(share_telegram)
                bot.send_video(message.chat.id, key_1, caption=f'Done ✅',
                               reply_markup=s)
        except:
            bot.reply_to(message, text='الرابط خطأ عزيزي!🚫')

#tiktok

sh_btn = types.InlineKeyboardButton(text='داگرتنی ڤیدیۆ', callback_data='s1')
version = types.InlineKeyboardButton(text='Version 1.1', callback_data='v')
dev = types.InlineKeyboardButton(text='کەناڵی بۆتەکان 🧑🏻‍💻🖤', url='t.me/MGIMT')

@bot.message_handler(commands=["tik"], chat_types=["private"])
def weclome(message):
    v = types.InlineKeyboardMarkup()
    v.row_width = 2
    v.add(sh_btn, version, dev)

    FIRST_NAME = message.from_user.first_name
    bot.send_message(message.chat.id, f'''
	*بەخێربێی ئەزیزم {FIRST_NAME}
 دەتوانی لە ڕێگایی دوگمە ڤیدیۆی تیکتۆك دابگریت*''', parse_mode='markdown', reply_markup=v)


@bot.callback_query_handler(func=lambda call: True)
def sh(call):
    if call.data == 's1':
        bot.send_message(call.message.chat.id, f"*ئێستا لینکی ڤیدیۆ بنێرە*", parse_mode="markdown")

    @bot.message_handler(func=lambda m: True)
    def Url(message):
        bot.send_message(message.chat.id, f"<strong>دادەبەزێت کەمێك چاوەڕێبە . . . ❗️</strong>", parse_mode="html")
        msg = message.text
        key_1 = requests.get(f'https://tikwm.com/api/?url={msg}').json()["UrlVideo"]
        bot.send_message(message.chat.id, text=f'''
		مبرمج الملف : {o}
     & قناة المبرمج : {p}''', parse_mode="MarkdownV2")
        try:
            if key_1 == False:
                bot.send_message(message.chat.id, f'- الرابط خطا عزيزي')
            else:
                share_telegram = types.InlineKeyboardButton(text='گۆڕینی بۆ دەنگ',
                                                            url='https://t.me/IQCVBOT?url=' + key_1)
                s = types.InlineKeyboardMarkup()
                s.row_width = 1
                s.add(share_telegram)
                bot.send_video(message.chat.id, key_1, caption=f'Done ✅',
                               reply_markup=s)
        except:
            bot.reply_to(message, text='الرابط خطأ عزيزي!🚫')


print('run')
bot.infinity_polling()
# تذكرو مصدري
'''
مبرمج الملف - @BRoK8
قناتي - @Crrazy_8
'''
