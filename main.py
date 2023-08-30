import requests, os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
try:
	import yt_dlp
except:
	os.system("pip install yt_dlp")
	import yt_dlp
	
api_id = 12962251 # Here Api Id 
api_hash = "b51499523800add51e4530c6f552dbc8" # Here Api Hash 
bot_token = "5853600134:AAEBZF6ZgSrpjYT2XnJKRwyLtt-EOtRV43Q" # Here Bot Token 
app = Client("iiu", api_id=api_id,api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start") & filters.private)
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

	 
@app.on_message(filters.text & filters.private)
async def download(client, message):
     EnyWeb = message.text 
     x = await message.reply("**دادەبەزێت کەمێك چاوەڕێبە . . . ❗️**")
     try:
       Media = yt_dlp.YoutubeDL({'format': 'best[ext=mp4]'}).extract_info(EnyWeb, False)["url"]
     except Exception as e:
        await x.delete()
        print(e)
        return await message.reply("**› لینك دروست نییە !**")
     try:
        caption = f"**داگرترا لەلایەن [بۆت](t.me/MGIMT) ♥️✅**"
        await message.reply_audio(
             Media,
             caption=caption
        )
        await x.delete()
     except Exception as e:
        print(e)
        await x.delete()
        return await message.reply("**هەڵەیە**")


print("Wait........")
app.run()
print("Bot is run")
    
#By @N0040
#Channel @B3kkk  
