import telebot
import requests, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import InlineKeyboardButton as Btn , InlineKeyboardMarkup as Mak
	
token = "5853600134:AAEBZF6ZgSrpjYT2XnJKRwyLtt-EOtRV43Q"#token
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"], chat_types=["private"])
def start(client, message):
 do = requests.get(f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id=@MGIMT&user_id={message.from_user.id}").text
    
 if do.count("left") or do.count("Bad Request: user not found"):
  return message.reply_text("**ببورە ئەزیزم پێویستە سەرەتا جۆینی [کەناڵی بۆت](t.me/MGIMT) بکەیت بۆ بەکارهێنانی بۆت\nدواتر /start بکە♥️✅**",
  disable_web_page_preview=True,
  reply_markup=InlineKeyboardMarkup(
  [[InlineKeyboardButton("⚡️ جۆینی کەناڵ بکە ئەزیزم ⚡️",
  url='https://t.me/MGIMT')]]))
 else:
    message.reply_photo(
        photo=f"https://telegra.ph/file/d2f5a8cf50eb98581f9e9.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 بۆتی داگرتن](t.me/MGIMT)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n\n**بەخێربێی ئەزیزم{message.from_user.mention} بۆ بۆتی داگرتن🕷️•**\n\n**تیکتۆك و ئینستاگرام بە شێوازی ڕاستەوخۆ دابگرا تەنیا لینکی بنێرە**\n\n**ڤیدیۆی پینترێست دابگرە لە ڕێگایی دوگمەوە**\n\n**نموونە :**\n**/pin بنووسە خۆی دوگمەت پێدەدات بۆ داگرتن**\n\n**دروستکراوم لەلایەن - [𐇮 ﺣّ͠ـِِّٓٓٔـەمّْٔــّ٘ە⤹🦅⃟آلـۘهہؚيـٰـُ͢ـُ໋۠بـ໋ۘ۠ه  𐇮](t.me/IQ7amo)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ پڕۆگرامساز", url=f"https://t.me/IQ7amo"),
                ], [

                InlineKeyboardButton(
                    "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT")

            ],

            ]

        ),

    )

	 
@bot.message_handler(func=lambda brok:True)
def Url(message):
		try:
			msgg = bot.send_message(message.chat.id, "*جاري التحميل ...*",parse_mode="markdown")
			msg = message.text
			url = requests.get(f'https://tikwm.com/api/?url={msg}').json()
			music = url['data']['music']
			region = url['data']['region']
			tit = url['data']['title']
			vid = url['data']['play']
			ava = url['data']['author']['avatar']
			##
			name = url['data']['music_info']['author']
			time = url['data']['duration']
			sh = url['data']['share_count']
			com = url['data']['comment_count']
			wat = url['data']['play_count']
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
			bot.send_photo(message.chat.id,ava,caption=f'- اسم الحساب : *{name}*\n - دوله الحساب : *{region}*\n\n- عدد مرات المشاهدة : *{wat}*\n- عدد التعليقات : *{com}*\n- عدد مرات المشاركة : *{sh}*\n- طول الفيديو : *{time}*',parse_mode="markdown")
			btn = Mak().add(Btn('تحميل الصوت',url=''+music))
			bot.send_video(message.chat.id,vid, caption=f"{tit}",reply_markup=btn)
		except:
			pass
			bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)
			bot.reply_to(message,'error );')


print('run')
bot.infinity_polling()
# تذكرو مصدري 
'''
مبرمج الملف - @BRoK8
قناتي - @Crrazy_8
'''
