import telebot
import requests
from telebot import types,TeleBot

TOK_BOT = ("5853600134:AAEBZF6ZgSrpjYT2XnJKRwyLtt-EOtRV43Q")#token
b = "MGIMT"
a = "@IQ7amo"
sh_btn = types.InlineKeyboardButton(text='داگرتن', callback_data='s1')
version = types.InlineKeyboardButton(text='Version 1.1', callback_data='v')
dev = types.InlineKeyboardButton(text='🧑🏻‍💻پڕۆگرامساز', url='tg://openmessage?user_id=833360381')

bot = telebot.TeleBot(TOK_BOT)
@bot.message_handler(commands=['pin'])
def weclome(message):
	b = types.InlineKeyboardMarkup()
	b.row_width = 2
	b.add(sh_btn,version, dev)
	
	FIRST_NAME = message.from_user.first_name
	bot.send_message(message.chat.id,f'''
	*- اهلن بك {FIRST_NAME}
 في بوت تحميل من بنترست 👾
& فقط اضغط تحميل*''',parse_mode='markdown',reply_markup=b)
	
@bot.callback_query_handler(func=lambda call: True)
def sh(call):
	if call.data=='s1':
		bot.send_message(call.message.chat.id,f'- ارسل الرابط!')
	@bot.message_handler(func=lambda m: True)
	def Url(message):
		bot.send_message(message.chat.id,f"<strong>Wait Please</strong>",parse_mode="html")
		msg = message.text
		key_1 = requests.get(f'https://dev-broksuper.pantheonsite.io/api/pin.php?url={msg}').json()["UrlVideo"]
		bot.send_message(message.chat.id,text=f'''
		مبرمج الملف : {a}
     & قناة المبرمج : {b}''',parse_mode="MarkdownV2")
		try:
			if key_1==False:
				bot.send_message(message.chat.id,f'- الرابط خطا عزيزي')
			else:
				share_telegram = types.InlineKeyboardButton(text='- مشاركه', url='https://t.me/share/url?url='+key_1)
				s = types.InlineKeyboardMarkup()
				s.row_width = 1
				s.add(share_telegram)
				bot.send_video(message.chat.id,key_1,caption=f'Done ✅',
    reply_markup=s)
		except:
			bot.reply_to(message,text='الرابط خطأ عزيزي!🚫')
print('run')
bot.infinity_polling()
