import telebot
import requests
from telebot import types, TeleBot
from telebot.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak

token = "5853600134:AAEBZF6ZgSrpjYT2XnJKRwyLtt-EOtRV43Q"  # token
bot = telebot.TeleBot(token)
# تذكرو مصدري
'''
مبرمج الملف - @BRoK8
قناتي - @Crrazy_8
'''
owner = 833360381  # Owner ID
users = []

p = "@MGIMT"
o = "@IQ7amo"
sh_btn = types.InlineKeyboardButton(text='داگرتنی ڤیدیۆ', callback_data='s1')
version = types.InlineKeyboardButton(text='Version 1.1', callback_data='v')
dev = types.InlineKeyboardButton(text='کەناڵی بۆتەکان 🧑🏻‍💻🖤', url='t.me/MGIMT')

@bot.message_handler(commands=["start"], chat_types=["private"])
def start(message):
    id = message.from_user.id
    channel = "MGIMT"  # Your channel username without @
    n = message.from_user.first_name
    u = message.from_user.username
    if message.chat.type == "private":
        if not id in users:
            users.append(id)
            stats = len(users)
            bot.send_message(owner,
                             "➕ Someone start Your bot :\n🪪 Name : {}\n💡 Username : {}\n🆔 User Id : {}\n\n➖ Users stats : {}".format(
                                 n, u, id, stats), disable_web_page_preview=True)
        x = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{channel}&user_id={id}").text
        if x.count("left") or x.count("Bad Request: user not found"):
            z = types.InlineKeyboardMarkup()
            x = types.InlineKeyboardButton(text="⚡️ جۆینی کەناڵ بکە ئەزیزم ⚡️", url=f"t.me/{channel}")
            z.add(x)
            return lol.send_message(message.chat.id, f'''<strong>- ببورە ئەزیزم پێویستە سەرەتا جۆینی کەناڵ بکەیت
-» جۆینی ئەم کەناڵە بکە @{channel} .
-» دواتر /start بنێرە  ✅ </strong>''', reply_markup=z, parse_mode='html')
        aa = types.InlineKeyboardMarkup()
        b = types.InlineKeyboardButton(text="᳒ᯓ پڕۆگرامساز", url=f"t.me/IQ7amo")
        aa.add(b)
        bot.send_message(message.chat.id,
                         f"*⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 بۆتی داگرتن*\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n\n*بەخێربێی ئەزیزم بۆ بۆتی داگرتن🕷️•*\n\n*تیکتۆك و ئینستاگرام بە شێوازی ڕاستەوخۆ دابگرا تەنیا لینکی بنێرە*\n\n*ڤیدیۆی پینترێست دابگرە لە ڕێگایی دوگمەوە*\n\n*نموونە :*\n*/pin بنووسە خۆی دوگمەت پێدەدات بۆ داگرتن*\n\n*@IQ7amo - دروستکراوم لەلایەن*",
                         parse_mode='markdown', reply_markup=aa, reply_to_message_id=message.message_id)


@bot.message_handler(func=lambda brok: True)
def Url(message):
    global msgg
    try:
        msgg = bot.send_message(message.chat.id, "*دادەبەزێت کەمێك چاوەڕێبە . . . ❗️*", parse_mode="markdown")
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
        bot.send_photo(message.chat.id, ava,
                       caption=f'*✧ ¦ ناو : {name}*\n*✧ ¦ وڵات : {region}*\n\n*✧ ¦ ژمارەی بینەر : {wat}*\n*✧ ¦ ژمارەی کۆمێنت : {com}*\n*✧ ¦ ژمارەی شەیرەکان : {sh}*\n*✧ ¦ درێژی ڤیدیۆ : {time}*',
                       parse_mode="markdown")
        btn = Mak().add(Btn('گۆڕینی بۆ دەنگ', url='https://t.me/IQCVBOT'))
        bot.send_video(message.chat.id, vid, caption=f"{tit}", reply_markup=btn)
    except:
        pass
        bot.delete_message(chat_id=message.chat.id, message_id=msgg.message_id)


@bot.message_handler(commands=["pin"], chat_types=["private"])
def weclome(message):
    v = types.InlineKeyboardMarkup()
    v.row_width = 2
    v.add(sh_btn, version, dev)

    FIRST_NAME = message.from_user.mention
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


print('run')
bot.infinity_polling()
# تذكرو مصدري
'''
مبرمج الملف - @BRoK8
قناتي - @Crrazy_8
'''
