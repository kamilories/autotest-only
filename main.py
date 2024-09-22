
import requests
test1 = {
            "name": "test1",
            "phone": "71111111111",
            "email": "test1@a.ru",
            "company": "test1",
            "budget": "Менее 2 млн", #2-3 млн 3–5 млн 5–10 млн 10-20 млн Более 20 млн
            "recommendation": "Рейтинги", # Копирайт на сайте Соцсети Рекомендации Давно знаю
            "description": "test1",
            "type": "Комплекс работ", #Сайт Сервис Дизайн UX-аудит Брендинг

        }
test2 = {
            "name": "test2",
            "phone": "71111111111",
            "email": "test2@a.ru",
            "company": "test2",
            "budget": "2-3 млн",
            "recommendation": "Копирайт на сайте",
            "description": "test2",
            "type": "Сайт",

        }

test3 = {
            "name": "test3",
            "phone": "71111111111",
            "email": "test3@a.ru",
            "company": "test3",
            "budget": "3–5 млн",
            "recommendation": "Соцсети",
            "description": "test3",
            "type": "Сервис",

        }

test4 = {
            "name": "test4",
            "phone": "71111111111",
            "email": "test4@a.ru",
            "company": "test4",
            "budget": "5–10 млн",
            "recommendation": "Рекомендации",
            "description": "test4",
            "type": "Дизайн",

        }

test5 = {
            "name": "test5",
            "phone": "71111111111",
            "email": "test5@a.ru",
            "company": "test5",
            "budget": "10-20 млн",
            "recommendation": "Давно знаю",
            "description": "test5",
            "type": "UX-аудит"

        }

test6 = {
            "name": "test6",
            "phone": "71111111111",
            "email": "test6@a.ru",
            "company": "test6",
            "budget": "10-20 млн",
            "recommendation": "Давно знаю",
            "description": "test6",
            "type": "Брендинг",

        }

def anketa(payload):
    # Прописываем инфу из network: header и payload
    Headers = {"accept": "application/json",
               "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36",
               "referer": "https://only.digital/",
               "origin": "https: // only.digital",
               "authorization": "0948081941de9b3cdead5e570118cbe30da14398f64bfa3556b6bd14e6d24416"

               }
    payload = payload

    # делаем пост запрос на json файл
    res = requests.post('https://api.only.digital/api/ru/brief/', json=payload, headers=Headers)

    result = res.json()
    print(res)
    print(result)



anketa(test1)
anketa(test2)
anketa(test3)
anketa(test4)
anketa(test5)
anketa(test6)
