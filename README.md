# Платформа для онлайн-обучения

## Запуск приложения
Заполнение базы данных произведено в админке. Создать суперпользователя кастомной командой 'python manage.py csu'. Заполнить базу данных командой `python manage.py loaddatautf8 data.json`. 

## Команды в терминале
- celery -A config worker -l INFO -P eventlet
- celery -A config beat -l INFO

## Примечание
Сервер доступен по адресу http://localhost:8001/

## 24.1 Вьюсеты и дженерики
## Запросы в Postman для курса
- POST: http://localhost:8000/course/ (заполнить тело, выбрав параметры 'raw' и 'json'; поля: name, description)
- GET: http://localhost:8000/course/<pk курса>/
- PUT: http://localhost:8000/course/<pk курса>/ (заполнить тело, выбрав параметры 'raw' и 'json')
- DELETE: http://localhost:8000/course/<pk курса>/

## Запросы в Postman для урока
- POST: http://localhost:8000/lesson/create/ (заполнить тело, выбрав параметры 'raw' и 'json', поля: name, description, course)
- GET (получить список уроков): http://localhost:8000/lesson/list/
- GET (получить конкретный урок): http://localhost:8000/lesson/view/<pk урока>/
- PATCH: http://localhost:8000/lesson/update/<pk урока>/
- DELETE: http://localhost:8000/lesson/delete/<pk урока>/

## 24.2 Сериализаторы
## Запросы в Postman для курса
- GET: http://localhost:8000/course/

## Запросы в Postman для пользователя
-GET (фильтровать по способу оплаты): http://localhost:8000/users/payment/list/?pay_approach=<значение> (в базе данных имеются str значения: 'наличными' и 'картой')
-GET (фильтровать по курсу): http://localhost:8000/users/payment/list/?payed_course=<значение> (в базе данных имеются int значения: 2 и 3)

## 25.1 Права доступа в DRF
## Запросы в Postman
- POST: http://localhost:8000/users/register/ (заполнить тело, выбрав параметры 'raw' и 'json', поля: email, password)

## 25.2 Валидаторы, пагинация и тесты
## Запросы в Postman
- POST (запрос токена): http://localhost:8000/users/token/ (пример тела: {"email": "admin@sky.pro", "password": "123qwe567rty"})
- POST (проверка ссылок на видео): http://localhost:8000/lesson/create/ (пример тела: {"name": "test video", "description": "test video", "course": 2, "url": "https://www.youtube.com/watch?v=FH-TzCVymb0&t=124s"})
- POST (зарегистрировать оплату подписки): http://localhost:8000/subscriptions/create/ (пример тела: {"is_subscribed": true, "course": 2})
- GET (вывод всех курсов с пагинацией): http://localhost:8000/course/
- GET (вывод всех уроков с пагинациец): http://localhost:8000/lesson/list/

## 26.1 Документирование и безопасность
Запросы в браузере
- http://localhost:8000/swagger/ (документация swagger)
- http://localhost:8000/redoc/ (документация redoc)

## Запросы в Postman
- POST (получить ссылку на оплату): http://localhost:8000/users/payment/create/ (пример тела: {"sum": 100000, "pay_approach": "карта", "payed_course": 2, "payed_lesson": 1})

## 26.2. Celery
Запросы в Postman
PUT: http://localhost:8000/course/<pk курса>/ (пример тела: {"name": "python", "description": "python разработчик"})

## 27.2. Docker Compose
Команды в терминале:
- docker-compose build (собрать образ);
- docker-compose up (запуск контейнера);
- docker-compose exec app <команда> (выполнение команды внутри контейнера)
