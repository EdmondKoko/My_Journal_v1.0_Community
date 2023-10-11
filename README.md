![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=yellow)
![Django](https://img.shields.io/badge/Django-2.2.9-red?style=for-the-badge&logo=django&logoColor=blue)
![SQLite](https://img.shields.io/badge/SQLite-grey?style=for-the-badge&logo=postgresql&logoColor=yellow)
![Pytest-django](https://img.shields.io/badge/pytest-django==3.8.0-orange?style=for-the-badge&logo=nginx&logoColor=green)

# Yatube - социальная сеть для публикации личных дневников. 

В проекте реализовано:
- Создано и зарегистрировано приложение Posts.
- Подключена база данных.
- Десять последних записей выводятся на главную страницу. 
- В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.
- Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

### Запуск приложения:

Клонируем проект:

```bash
git clone https://github.com/edmondkoko/hw02_community.git
```

Переходим в папку с проектом:

```bash
cd hw02_community
```

Устанавливаем виртуальное окружение:

```bash
python3 -m venv venv
```

Активируем виртуальное окружение:

```bash
source venv/bin/activate
```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

Создаем супер пользователя:

```bash
python manage.py createsuperuser
```

Запускаем проект:

```bash
python manage.py runserver
```

После чего проект будет доступен по адресу (http://127.0.0.1:8000/)
