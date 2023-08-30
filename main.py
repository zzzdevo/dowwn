import requests
import json
import telebot
from user_agent import generate_user_agent
token = "5853600134:AAEBZF6ZgSrpjYT2XnJKRwyLtt-EOtRV43Q"
bot = telebot.TeleBot(token)

headers = {
'authority': 'reelsaver.net',
'accept': '*/*',
'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://reelsaver.net',
'referer': 'https://reelsaver.net/download-reel-instagram',
'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': generate_user_agent(),
'x-requested-with': 'XMLHttpRequest',
}#@Crrazy_8 & @BRoK8
@bot.message_handler(commands=["start"])
def Welcome(message):
 name = message.from_user.first_name
 bot.reply_to(message,f'''- مرحبا بك [{name}](tg://settings)
- في بوت تحميل من الانستكرام 
- لتحميل (الفديوهات) ارسل رابط المنشور''',parse_mode="markdown")
@bot.message_handler(content_types=['text'])
def video(message):
    link = message.text
    data = {
    'via': 'form',
    'ref': 'download-reel-instagram',
    'url': link,
    }#@Crrazy_8 & @BRoK8
    response = requests.post('https://reelsaver.net/api/instagram', headers=headers, data=data).json()
    No = response['success']
    if No == False:
     bot.reply_to(message,'<i>خطأ تأكد من الرابط ..</i>',parse_mode="html")
    else:
     bot.send_chat_action(message.chat.id,action='upload_video')
     #user = response['data']['user']['username']
     video = response["data"]['medias'][0]['src']
     #log = response['data']['medias'][0]['preview_src']
     bot.send_video(message.chat.id,video , reply_to_message_id=message.message_id)

bot.infinity_polling()
