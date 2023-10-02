import requests
import telebot
from time import sleep
from telebot import types
Owner = '5136116009'
User_Ch = 'old_school_team'
bot = telebot.TeleBot("6501680766:AAE-G-BU1-VMjJfXTfmWPdUM_jlhKRgA83w")
@bot.message_handler(commands=['start'])
def start(message):
  Id_Member = message.from_user.id
  Check_Member = requests.get(f"https://api.telegram.org/bot6501680766:AAE-G-BU1-VMjJfXTfmWPdUM_jlhKRgA83w/getchatmember?chat_id=@{User_Ch}&user_id={Id_Member}").text
  if Id_Member == Owner or "member" in Check_Member or "creator" in Check_Member or "administrator" in Check_Member:
    bot.reply_to(message,"- Welcome To Flikers BOT\n\n- This Bot Give You Unlimited FaceBook Likes\n\n- Programer : @WHI3PER\n\n- Send Facebook Cookies")
  else:
    	For_Channel =types.InlineKeyboardMarkup()
    	CH= types.InlineKeyboardButton('قناة البوت',url="t.me/"+str(User_Ch))
    	For_Channel.add(CH)
    	bot.reply_to(message,'- مش مشترك و تريد تستعمل البوت ؟؟',reply_markup=For_Channel)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global co
    co = str(message.text)
    response = requests.post('https://flikers.net/android/android_check_new_cookie.php',headers={"Cookie": co, "Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; Plume L2 Build/O00623)","Host": "flikers.net", "Connection": "Keep-Alive", "Accept-Encoding": "gzip","Content-Length": "0"}).json()
    if response['status'] == 'SUCCESS':
        name = response['name']
        msg = str(response['message'])
        country = response['country']
        keyboard=[[types.InlineKeyboardButton("Haha 😂", callback_data='HAHA'),types.InlineKeyboardButton("Love ❤️", callback_data='LOVE'),types.InlineKeyboardButton("Like 👍🏻", callback_data='LIKE'),],[types.InlineKeyboardButton("Angry 😡", callback_data='ANGRY'),types.InlineKeyboardButton("Care 🤗", callback_data='CARE'),types.InlineKeyboardButton("Wow 😲", callback_data='WOW'),],]
        reply_markup = types.InlineKeyboardMarkup(keyboard)
        bot.send_message(message.chat.id,f'- {msg}\n\n- Name : {name}\n\n- Country : {country}\n\n- Choose Reaction', reply_markup=reply_markup)
    else:
        msg = response['message']
        bot.reply_to(message, f"- {msg}")
@bot.callback_query_handler(func=lambda call: True)
def button(call):
    link = bot.send_message(call.message.chat.id, "- Send Post Link")
    bot.register_next_step_handler(link, handle_link, call)
def handle_link(message, call):
    link = message.text
    type = call.data
    data = '{"post_id":"' + link + '","react_type":"' + type + '"}'
    res1 = requests.post('https://flikers.net/android/android_get_react.php', data=data, headers={"Cookie": co, "Content-Type": "application/x-www-form-urlencoded","User-Agent": "Dalvik/2.1.0 (Linux; U; Android 8.0.0; Plume L2 Build/O00623)","Host": "flikers.net", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "Content-Length": str(len(data))}).json()
    if res1['status'] == 'SUCCESS':
        msg = res1['message']
        bot.reply_to(message, f"- {msg}")
    else:
        msg = res1['message']
        bot.reply_to(message, f"- {msg}")
bot.polling()
