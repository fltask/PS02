import requests

print('*' * 10, 'Задание 2', '*' * 10)
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}

response = requests.get(url, params=params)

if response.ok:
    posts = response.json()
    print(f"Найдено {len(posts)} записей для userId=1:\n")
    for post in posts:
        print(f"ID: {post['id']}")
        print(f"Заголовок: {post['title']}")
        print(f"Текст: {post['body']}\n")
else:
    print(f"Ошибка: статус-код {response.status_code}")
