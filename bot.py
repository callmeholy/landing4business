import telebot
from tokens import bot_token, user_id


bot = telebot.TeleBot(bot_token)




def send_notification(name, number):
    try:
        bot.send_message(user_id, f'Вам пришла новая заявка:\nИмя: {name}\nТелефон: {number}')
    except Exception as e:
        print(f'Ошибка при отправке: {e}')

