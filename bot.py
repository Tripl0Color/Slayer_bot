from random import randint
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import pyowm
import datetime
from pycbrf.toolbox import ExchangeRates
from nickname_generator import generate



vk_session = vk_api.VkApi(token='token')

owm = pyowm.OWM('token',language = "RU")

user_token = '' #vk user token



longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
ban_list = ['хуй','Хуй','пизда','Сука','еблан','дебил','идиот','пезда','хуесос','пиздется','хуево','cock','idiot','eblan','хуело']
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text in ban_list:
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Не матерись'
		)
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=event.random_id,
                    message='Не матерись'
        )

        if event.text == 'погода' or event.text == 'Погода':
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Введите город🌏'
		)
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    random_id=event.random_id,
                    message='Введите город🌏'
       )
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    observation = owm.weather_at_place(event.text)
                    w = observation.get_weather()
                    temp = w.get_temperature('celsius')["temp"]
                    if event.from_user:
                        vk.messages.send(
                            user_id=event.user_id,
                            random_id=event.random_id,
                            message="В городе " +  event.text  + "🌆  " + "сейчас " + w.get_detailed_status() +'.' + "\nTемпература " + str(temp)+" °C"
        		)
                    break
                elif event.from_chat:
                    observation = owm.weather_at_place(event.text)
                    w = observation.get_weather()
                    temp = w.get_temperature('celsius')["temp"]
                    vk.messages.send(
                        chat_id=event.chat_id,
                        random_id=event.random_id,
                        message="В городе " +  event.text  + "🌆  " + "сейчас " + w.get_detailed_status() +'.' + "\nTемпература " + str(temp)+" °C"
        	    )
                    break

        if event.text == 'Курс' or event.text == 'курс':
            #получение курса
            time = datetime.datetime.now()
            rates = ExchangeRates(time)

            cource_uah = rates['UAH'].rate

            cource_czk = rates['CZK'].rate

            cource_jpy = rates['JPY'].rate

            course = rates['USD'].rate

            course_eur = rates['EUR'].rate
            if event.from_user:
                vk.messages.send(
                user_id=event.user_id,
                random_id=event.random_id,
                message='Курс\nДоллар ' + str(course) + '\n' + 'Евро ' + str(course_eur) + '\n' + 'Гривна ' +  str(cource_uah) + '\n' + 'Чеш.крона ' + str(cource_czk) + '\n' + 'Япон.иена ' + str(cource_jpy)
        		)



        if event.text == '/help' or event.text == 'помощь' or event.text == 'Помощь':
            vk.messages.send(
            user_id=event.user_id,
            random_id=event.random_id,
            message='В этой статье описаны все комманды бота - https://vk.com/@-194867465-komandy-bota'
            )

        if event.text == 'Ник' or event.text == 'ник':
           vk.messages.send(
           user_id=event.user_id,
           random_id=event.random_id,
           message='Сгенерировал ' + generate()
           )

        if event.text == 'Размер' or event.text == 'размер':
          cock = randint(1,20)
          vk.messages.send(
          user_id=event.user_id,
          random_id=event.random_id,
          message='Твой  член ' + str(cock) + 'cm'
         )

        if event.text == 'slayer' or event.text == 'Слейр':
            vk.messages.send(
            user_id=event.user_id,
            random_id=event.random_id,
            message='я тут'
          )
	
	if event.text == 'iq' or event.text == 'IQ':
           iq = randint(40,200)
           vk.messages.send(
           user_id=event.user_id,
           random_id=event.random_id,
           message='Ваш iq ' + str(iq)
           )
	
	if event.text == 'Профиль' or event.text == 'профиль':
            if str(event.user_id) == admin_id:
                vk.messages.send(
                user_id=event.user_id,
                random_id=event.random_id,
                message='Твой профиль:\nID:' + str(event.user_id) + '\n Твоя роль:Admin💎'
              )

            elif str(event.user_id) != admin_id:
                vk.messages.send(
                user_id=event.user_id,
                random_id=event.random_id,
		message='Твой профиль:\nID:' + str(event.user_id) + '\n Твоя роль: User💡' + '\nПредупреждений: ' +  str(warnings) + '❌' 
              )
