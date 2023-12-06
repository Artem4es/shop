## [Лендинг-страница с формой заказа](https://turbotyoma.ru) :motorcycle:
Страница, на которой размещена информация о компании, предоставляющей услуги прошивки мотоциклов. На сайте доступна форма заказа при заполнении которой, отправляется уведомление в Telegram о новом заказе и заказ сохраняется в БД. Стек технологий Django 4, Telegram API, Docker, Bootstrap 5.


### Как развернуть проект: :question:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Artem4es/shop.git
```

```
cd shop
```

Cоздать файл с переменными окружения .env:

```
TOKEN=                  # Токен TG бота
ADMIN_ID=               # ID админа в телеграм
RECAPTCHA_PUBLIC_KEY=
RECAPTCHA_PRIVATE_KEY=

```

Запустить проект в docker
```
docker-compose up --build
```

Вуаля!


