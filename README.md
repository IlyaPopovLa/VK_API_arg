# Обрезка ссылок с помощью VK

1. Сокращение ссылки:
    Выполнить в терминале ```python main.py 'ссылка для сокращения'```
2. Получение статистики:
    Выполнить в терминале ```python main.py 'сокращенная ссылка'```

### Установка

1. Скопировать репозиторий к себе:
    https://github.com/IlyaPopovLa/VK_API
2. Python3 должен быть уже установлен.
3. Выполнить установку зависимостей:
    ```pip install -r requirements.txt``` (необходимые библиотеки requests, python-dotenv)
4. Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)
5. Создайте файл .env и добавьте ваш VK API токен:
    ```VK_TOKEN='ваш_токен_здесь'```

### Цель проекта

1. Данный скрипт сокращает длинные URL-ссылки через VK API
2. Получает статистику кликов по уже сокращённым ссылкам
