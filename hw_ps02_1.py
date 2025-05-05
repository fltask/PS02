from pprint import pprint

import requests

print('*' * 10, 'Задание 1', '*' * 10)
# Задаем параметры запроса
url = "https://api.github.com/search/repositories"
params = {"q": "html"}
headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"  # Укажите свое приложение
}

# Отправляем GET-запрос
response = requests.get(url, headers=headers, params=params)

# Выводим статус-код ответа
print("Статус-код:", response.status_code)

# Выводим содержимое ответа в формате JSON
print("JSON-ответ:")
pprint(response.json())
print('-' * 100, '\n')
