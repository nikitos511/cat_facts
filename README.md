# Cat Facts Script

Простой скрипт на Python для работы с публичным API [catfact.ninja](https://catfact.ninja/).

## Задание
- Получить список фактов о котах.
- Определить общее количество фактов и последнюю страницу.
- Скачать последнюю страницу.
- Вывести самый короткий факт.

## Требования
- Python 3.9.13
- Библиотека `requests`

## Установка и запуск

### Клонировать репозиторий:
```
bash

git clone https://github.com/<your-username>/catfacts-script.git
cd catfacts-script
```

### Создать виртуальное окружение (опционально):
```
bash

python -m venv venv
```
### для Linux/Mac
```
bash

source venv/bin/activate
```
### для Windows
```
bash

venv\Scripts\activate
```
### Установить зависимости:
```
bash

pip install -r requirements.txt
```
### Запустить скрипт:
```
bash

python catfacts.py
```