Проект **news_app**

## Описание
=====================
Новостное приложение с использованием DRF (Django Rest Framework).
Проект содержит две базы данных: новости и типы новостей.

##### Структура базы данных новостей:
* Имя;
* Краткое описание;
* Полное описание;
* Тип новости.

##### Структура базы данных типов новостей:
* Имя;
* Цвет.

#### Функционал проекта:
* CRUD (Create, Read, Update, Delete) типов новостей;
* CRUD новостей;
* Получение списка всех типов новостей;
* Получение списка всех новостей вида:
    * Имя;
    * Краткое описание;
    * Имя типа;
    * Цвет типа.
* Получение списка новостей определенного типа.

### Примеры
POST запрос на создание типа новостей:

```javascript
{
    "name": "Происшествия",
    "color": "#EFFC26"
}
```

POST запрос на создание новости:

```javascript
{
    "name": "Событие",
    "short_description": "Краткое описание",
    "full_description": "Полное описание",
    "type": "Происшествия"
}
```

GET запрос получение списка всех типов новостей:
```javascript
[
    {
        "name": "Спорт",
        "color": "#EFFC2D"
    },
    {
        "name": "Событие",
        "color": "#EFFC28"
    },
    {
        "name": "Происшествия",
        "color": "#EFFC26"
    }
]
```

Окружение для работы с базой данных
-----------------------------------
### Инструкция по заполению .env

```
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Docker
-----------------------------------
### Инструкция по установке Docker

[Ссылка](https://docs.docker.com/engine/install/ubuntu/)


Команды
-----------------------------------

### Команда клонирования проекта с DockerHub

`sudo docker pull upamid/yamdb_final`

### Команда для запуска приложения

`docker-compose up -d --build `

### Команда запуска docker-compose

`docker-compose up`

### Команда миграции базы данных

`docker-compose exec web python manage.py migrate --noinput`

### Команда для создания суперпользователя

`docker-compose exec web python manage.py createsuperuser`

### Команда для заполнения базы начальными данными

`docker-compose exec web python manage.py loaddata fixtures.json`

### Команда для остановки приложения

`sudo docker-compose stop`

# участник

[Дмитрий Ступницкий.](https://github.com/upamid) 
