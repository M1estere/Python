import telebot
import config
import random
import requests

from telebot import types
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot(config.TOKEN)

response = requests.get(config.url).json()

@bot.message_handler(commands=['help']) #Команда помощи /help
def mess(message):

	sti3 = open('static/AnimatedSticker3.tgs', 'rb')
	sti2 = open('static/AnimatedSticker2.tgs', 'rb')

	bot.send_sticker(message.chat.id, sti2)

	markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
	item1 = types.KeyboardButton("Почта создателя")
	item2 = types.KeyboardButton("Контактный телефон")
	item3 = types.KeyboardButton("/restart")
	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, 'Здесь я скоро буду помогать, не скучай, {0.first_name}! \n Можешь сделать что-то \n Если нужно вернуться - набери /restart'.format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup = markup)

@bot.message_handler(commands = ['restart'])

def res(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 4)
	item1 = types.KeyboardButton("🙃 Случайное число")
	item2 = types.KeyboardButton("😁 Как дела?")
	item3 = types.KeyboardButton("💰 Курсы валют")
	item4 = types.KeyboardButton("😂 Анекдот")
	item5 = types.KeyboardButton("💪 Супергерои")
	# item6 = types.KeyboardButton("🕺 Разговорчики")
	item7 = types.KeyboardButton("🤳 Стикеры")		
	item8 = types.KeyboardButton("👓 Погода")

	markup.add(item1, item2, item3, item4, item5, item7, item8)

	bot.send_message(message.chat.id, "Давай начнем сначала, {0.first_name}!\nЯ - <b>{1.first_name}</b>, простой полезный бот.".format(message.from_user, bot.get_me()), 
		parse_mode='html', reply_markup = markup)

@bot.message_handler(commands=['start', 'restart']) #Команда начала /start


def welcome(message):
	sti = open('static/AnimatedSticker.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 4)
	item1 = types.KeyboardButton("🙃 Случайное число")
	item2 = types.KeyboardButton("😁 Как дела?")
	item3 = types.KeyboardButton("💰 Курсы валют")
	item4 = types.KeyboardButton("😂 Анекдот")
	item5 = types.KeyboardButton("💪 Супергерои")
	# item6 = types.KeyboardButton("🕺 Разговорчики")
	item7 = types.KeyboardButton("🤳 Стикеры")		
	item8 = types.KeyboardButton("👓 Погода")

	markup.add(item1, item2, item3, item4, item5, item7, item8)

	msg = bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, простой полезный бот.".format(message.from_user, bot.get_me()), 
		parse_mode='html', reply_markup = markup)
	bot.register_next_step_handler(msg, process_coin_step)

@bot.message_handler(content_types=["text"])


def process_coin_step(message):
	try:

		markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 3)
		item1 = types.KeyboardButton("USD")
		item2 = types.KeyboardButton("EUR")
		item3 = types.KeyboardButton("BTC")
		item4 = types.KeyboardButton("/restart")


		markup.add(item1, item2, item3, item4)

		for coin in response:
			if (message.text == coin['ccy']):
				bot.send_message(message.chat.id, printCoin(coin['buy'], coin['sale']), reply_markup = markup, parse_mode = "Markdown")
		
		sti4 = open('static/AnimatedSticker4.tgs', 'rb')

		'''if message.text == '🕺 Разговорчики':

			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton("Смысл жизни", callback_data='life')

			markup.add(item1)

			bot.send_message(message.chat.id, "Вот на такие темы мы с тобой можем поговорить, {0.first_name}!".format(message.from_user, bot.get_me()), reply_markup=markup) '''		

		if message.text == '💪 Супергерои':
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=2)
			item1 = types.KeyboardButton("🕷 Человек-паук")
			item2 = types.KeyboardButton("🦇 Бэтмен")
			item3 = types.KeyboardButton("⚡ Флэш")
			item4 = types.KeyboardButton("🔞 Дэдпул")
			item5 = types.KeyboardButton("/restart")


			markup.add(item1, item2, item3, item4, item5)

			bot.send_message(message.chat.id, "Вот этих супергероев я знаю!\n Неужели ты думаешь, что любишь их больше, чем я, {0.first_name}?".format(message.from_user,bot.get_me()), reply_markup=markup)

		elif message.text == '🤳 Стикеры':

			bot.send_message(message.chat.id, 'Скоро смогу отправлять стикеры, а пока опробуй другие функции этого бота')

		elif message.text == '🙃 Случайное число':

			bot.send_message(message.chat.id, str(random.randint(0, 1000)))

		elif message.text == '😁 Как дела?':

			markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width=2)

			item1 = types.KeyboardButton("Хорошо 😎")
			item2 = types.KeyboardButton("Не очень 😣")
			item3 = types.KeyboardButton("Приболел 😷")
			item4 = types.KeyboardButton("Пьян 🥴")
			item5 = types.KeyboardButton("/restart")

			markup.add(item1, item2, item3, item4, item5)

			bot.send_message(message.chat.id, "Отлично, сам как?".format(message.from_user,bot.get_me()), reply_markup=markup)

		elif message.text == 'Хорошо 😎':
			bot.send_message(message.chat.id, 'Вот и молодец 😊')
		elif message.text == 'Не очень 😣':
			bot.send_message(message.chat.id, 'Крепись 👊')
		elif message.text == 'Приболел 😷':
			bot.send_message(message.chat.id, 'Выздоравливай 😟')
		elif message.text == 'Пьян 🥴':
			bot.send_message(message.chat.id, 'Выпей ещё 🥃')

		elif message.text == '💰 Курсы валют':

			bot.send_message(message.chat.id, "Чтобы узнать курс валюты, \n просто напиши её название, {0.first_name} \n А чтобы выйти нужно набрать /restart".format(message.from_user,bot.get_me()), reply_markup=markup)

		elif message.text == '😂 Анекдот':
			bot.send_message(message.chat.id, str(random.SystemRandom().choice(["Перенесли дату окончания Второй мировой - перенесём и пандемию!", "В период карантина рубль соблюдает режим самодевальвации, а экономика - самоликвидации.", "В сталинском доме проще соблюдать режим.", "Деньги - большой грех! - сказал патриарх K. - Но я спасу вас, взяв ваши грехи на себя!", "Время на раскачку, наконец-то, появилось! Но денег на раскачку, как оказалось, нет..."])))
			bot.send_sticker(message.chat.id, sti4)

		elif message.text == '👓 Погода':
			r = requests.get('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0')
			html = BS(r.content, 'html.parser')

			for el in html.select('#content'):
				t_min = el.select('.temperature .min')[0].text
				t_max = el.select('.temperature .max')[0].text
				text = el.select('.wDescription .description')[0].text

    		# убрать клавиатуру
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
			item1 = types.KeyboardButton("/restart")

			markup.add(item1)

			bot.send_message(message.chat.id, "Вот погода на сегодня: \n" +
				t_min + ', ' + t_max + '\n' + text, reply_markup=markup)

		elif message.text == "Почта создателя":
			bot.send_message(message.chat.id, "Вот почта разработчика: \n 7156643@mail.ru")

		elif message.text == "Контактный телефон":
			bot.send_message(message.chat.id, "Вот номер разработчика: \n 8(905)715-66-43")

		elif message.text == '🕷 Человек-паук':
			bot.send_message(message.chat.id, 'Челове́к-пау́к, настоящее имя Пи́тер Па́ркер — персонаж, супергерой, появляющийся в комиксах издательства Marvel Comics, созданный Стэном Ли и Стивом Дитко. С момента своего первого появления на страницах комикса Amazing Fantasy №15 он стал одним из самых популярных супергероев.')
		
		elif message.text == '🦇 Бэтмен':
			bot.send_message(message.chat.id, 'Бэ́тмен, изначально Бэт-мен — супергерой, персонаж комиксов издательства DC Comics, впервые появившийся в Detective Comics № 27 30 марта 1939 года, Бэтмен является одним из самых популярных и известных героев комиксов. Был создан художником Бобом Кейном в соавторстве с писателем Биллом Фингером')
		
		elif message.text == '⚡ Флэш':
			bot.send_message(message.chat.id, 'Флэш — американский телесериал, транслируемый каналом The CW и разработанный Грегом Берланти, Эндрю Крайсбергом и Джеффом Джонсом. Основан на супергерое DC Comics по прозвищу Флэш, который был создан Робертом Кнайгером, Джоном Брумом и Кармином Инфантино.')
		
		elif message.text == '🔞 Дэдпул':
			bot.send_message(message.chat.id, 'Уэйд Уилсон — наёмник. Будучи побочным продуктом программы вооружённых сил под названием «Оружие X», Уилсон приобрёл невероятную силу, проворство и способность к исцелению. Но страшной ценой: его клеточная структура постоянно меняется, а здравомыслие сомнительно. Всё, чего Уилсон хочет, — это держаться на плаву в социальной выгребной яме. Но течение в ней слишком быстрое.')
	
	except Exception as e:
		print(repr(e))

def printCoin(buy, sale):
	return "Курс покупки: " + str(buy) + "\n Курс продажи: " + str(sale)


''' def callback_inline(call):
	if call.message:
		if call.data == 'life':
			bot.send_message(call.message.chat.id, 'Смысла жизни нет, точнее, он есть, но для каждого он свой, и самое главное для человека - его поиск.\n А ты что думаешь?')
			
			#Убрать выпадающие кнопки, заменив их на текст
		bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 А как у тебя дела?",
								  reply_markup=None) '''




#Запуск
bot.polling(none_stop=True)