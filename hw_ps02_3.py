import requests

print('*' * 10, 'Задание 3', '*' * 10)
# Задаем URL и данные для отправки
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Отправляем POST-запрос с JSON-данными
response = requests.post(url, json=data)

# Проверяем успешность запроса
if response.ok:
    print("Запись успешно создана:")
    print(f"Статус-код: {response.status_code}")
    print(f"Ответ: {response.json()}")
else:
    print(f"Ошибка при создании записи: статус-код {response.status_code}")
