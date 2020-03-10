
import telebot 
import json 
from random import randint 
from telebot import types 

bot = telebot.TeleBot('987047113:AAG1S0FYlCJcqBjWlAoWsZuhTTzsbehJ6iE')


# Пишем @BotFather /mybots, выбираем своего бота, жмём Edit bot, а потом Edit Botpick и всё.

number = 0
tries = 6


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

'''Получаем имя пользователя'''
def get_name(message):
    global name
    
    name = message.text

    keyboard = types.InlineKeyboardMarkup() # Создает кнопку 1-100
    button_1 = types.InlineKeyboardButton(text="1-100", callback_data="100")
    keyboard.add(button_1)
    button_2 = types.InlineKeyboardButton(text="1-1000", callback_data="1000")
    keyboard.add(button_2)
    button_3 = types.InlineKeyboardButton(text="1-100000", callback_data="100000")
    keyboard.add(button_3)

    bot.send_message(message.chat.id, f"Привет, {name.title()}! Я загадаю число от: ", reply_markup=keyboard)
    # bot.register_next_step_handler(message, get_answer)

'''Генерируем числа от ...-...'''
def generate_number(num):
    x = randint(0, num)
    return x

def get_answer(message): #получаем chislo-otvet
    global tries
    answer = message.text
    try:
        if tries > 0:

            if int(answer) == number:
                bot.send_message(message.chat.id, 'Поздравляю! Ты угадал!')
                tries = 6
                bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIawF4sQHkOG4nf8OqTm70rIYjJWoonAAJPCQACeVziCSrbajXBvt7aGAQ')

                keyboard1 = types.InlineKeyboardMarkup()
                key_yes = types.InlineKeyboardButton(text="Повторить", callback_data="yes")
                keyboard1.add(key_yes)
                key_no = types.InlineKeyboardButton(text="Закончить", callback_data="no")
                keyboard1.add(key_no)                
                bot.send_message(message.chat.id, "Повторить? ", reply_markup=keyboard1)
            elif int(answer) > number:
                bot.send_message(message.chat.id, 'Мое число меньше!')
                tries -= 1
                bot.register_next_step_handler(message, get_answer)          
            
            elif int(answer) < number:
                bot.send_message(message.chat.id, 'Мое число больше!')
                tries -= 1
                bot.register_next_step_handler(message, get_answer)
        else:
            bot.send_message(message.chat.id, f'{name.title()}, ты проиграл! ')
            tries = 6
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIaxl4sQN7_f5ijCFvm0iQdBusKBYmsAAJbCQACeVziCec-bBWISvUfGAQ')
           
            keyboard1 = types.InlineKeyboardMarkup()
            key_yes = types.InlineKeyboardButton(text="Повторить", callback_data="yes")
            keyboard1.add(key_yes)
            key_no = types.InlineKeyboardButton(text="Закончить", callback_data="no")
            keyboard1.add(key_no)
            bot.send_message(message.chat.id, "Повторить? ", reply_markup=keyboard1)
    except ValueError:
        bot.send_message(message.chat.id, 'ДУРАК, ВВЕДИ ЧИСЛО!')
        bot.register_next_step_handler(message, get_answer)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIavl4sQFxng93gfEERm3ApYWx7VmfTAAJLCQACeVziCcmmZFmMW-h4GAQ')
            
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        global number
        if call.data == "100":
            number = generate_number(100)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введи свое число: ")
            bot.register_next_step_handler(call.message, get_answer)
    
        elif call.data == "1000":
            number = generate_number(1000)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введи свое число: ")
            bot.register_next_step_handler(call.message, get_answer)

        elif call.data == "100000":
            number = generate_number(100000)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Введи свое число: ")
            bot.register_next_step_handler(call.message, get_answer)

        elif call.data == "yes": 
            bot.send_message(call.message.chat.id, 'Как тебя зовут?')
            bot.register_next_step_handler(call.message, get_name)
        elif call.data == "no":
            bot.send_message(call.messagechat.id., f'Пока, {name.title()} \nНапиши /start, чтобы начать заново)')

    elif call.inline_message_id:
        if call.data == "100":
            number = generate_number(100)
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Введи свое число: ")
            bot.register_next_step_handler(call.message, get_answer)
        elif call.data == "1000":
            number = generate_number(1000)
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Введи свое число: ")
            bot.register_next_step_handler(call.message, get_answer)

        elif call.data == "100000":
            number = generate_number(100000)
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Введи свое число: ")
            bot.register_next_step_handler(call.message, get_answer)
        elif call.data == "yes": 
            bot.send_message(call.message.chat.id, 'Как тебя зовут?')
            bot.register_next_step_handler(call.message, get_name)
        elif call.data == "no":
            bot.send_message(call.message.chat.id, f'пока, {name.title()} )')


bot.polling()