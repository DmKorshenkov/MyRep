import telebot

bot = telebot.TeleBot('5707737301:AAEZITSr8ZNuwjhmyxAK2cqzkqwetOGNlxM')
new_dict = {}

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b><u>{message.from_user.username}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.chat.id not in new_dict:
        new_dict[message.chat.id] = [message.text]
    else:
        new_dict[message.chat.id] += [message.text]
    print(new_dict)

#def get_user_text(message):
#       bot.send_message(message.chat.id, message.text, parse_mode='html')


bot.polling(none_stop=True)
