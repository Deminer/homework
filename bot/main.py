import telebot
import requests

step = 'idle'

bot = telebot.TeleBot('1496099314:AAFU4Uqh7EUotkpZhBj4_QI2cdMOS5GiLlM')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global step

    # Если мы перешли на шаг создания коротких ссылок, то создаём ссылку и выходим из режима
    if step == "url":
        data = {
            'url': message.text
        }
        response = requests.post('https://cleanuri.com/api/v1/shorten', data=data)
        # print(response.json())
        bot.send_message(message.from_user.id, response.json()['result_url'])

    elif step == 'idle':
        if message.text.lower().find("start") != -1:
            bot.send_message(message.from_user.id, "Привет!")
        elif message.text.lower().find("url") != -1:
            step = 'url'
            bot.send_message(message.from_user.id, "Создание короткой ссылки. Пришли URL")
        else:
            bot.send_message(message.from_user.id, "Не понимаю")

bot.polling(none_stop=True, interval=0)