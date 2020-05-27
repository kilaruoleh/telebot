import telebot, random
bot = telebot.TeleBot('1279354182:AAEQ0oeUr6hyd2WEVgAhjgxnAl5uoaUN4CQ')

all_replies = {
1:'CAACAgIAAxkBAALiE17OYR0V8X9dR-tpzP9GsRoiuizvAALVAANa44oXpsPY0m9MkokZBA', 2:'CAACAgIAAxkBAALiFV7OYTwZxx3evGUvBCoj_KXohOYdAAIHAgACcQtCBa9ymI2KNbptGQQ', 
3:'CAACAgIAAxkBAALiF17OYUeBGRQoOBb_BqdGy6gyA2L2AAIDAAN9CosOepl5ogYKXhUZBA', 4:'CAACAgIAAxkBAALiGV7OYU9qoqGDzpuGZhcRVYzrLo_zAALPAANa44oXNfh47ULXjM4ZBA', 
5:'CAACAgIAAxkBAALiG17OYVqpVnCvLnDrHoXReLAAAR2u_gAC0QADWuOKFwe70Oy_Xr9rGQQ', 6:'CAACAgIAAxkBAALiHV7OYWJcc2MqeV8Lc5fJwm-mhlpBAAI0AAN_J6wOycmDqUO4Kt4ZBA', 
7:'CAACAgUAAxkBAALiH17OYWg8ri07Dn2sb_g1Ugz1EAqiAAKOAwAC6QrIA1cCvGXdZqpSGQQ', 8:'CAACAgIAAxkBAALiIV7OYddGDXpsjXRK2pO3Gkjr3N6vAAL9AANa44oXGN4aha0l7yEZBA', 
9:'CAACAgIAAxkBAALiI17OYd0nMchB2mjMGu00q1DSMhSsAAICAQACVp29Ck7ibIHLQOT_GQQ', 10:'CAACAgIAAxkBAALiJV7OYeOOB-ARO8hNnRzCgSUNjuk7AAKaCAACXAJlA8nAtczSRduMGQQ',
11:'Хмммм', 12:'Лол', 13:'Ахахахах', 14:'Кек', 15:'Тазашо', 16:'Шо', 17:'Ти шо жмых'
}

def choose_reply(message):
    number = random.randint(1, 17)
    if number > 10:
        return bot.send_message(message.chat.id, all_replies[number])
    else:
        return bot.send_sticker(message.chat.id, all_replies[number])

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAALiJ17OYxEu1tggbAvSikvE5AYn4PoyAAIlAwAC5s5WDAYJXeBfSI00GQQ')

@bot.message_handler(content_types=['text', 'audio', 'photo', 'sticker', 'video', 'voice'])
def echo_all(message):
    choose_reply(message)

@bot.message_handler(content_types='dice')
def send_dice(message):
    bot.send_dice(message.chat.id)

bot.polling(none_stop=False, interval=0, timeout=20)