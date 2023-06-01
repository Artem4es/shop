## [Лендинг-страница с формой заказа](https://turbotyoma.ru) :motorcycle:
Страница, на которой размещена информация о компании, предоставляющей услуги прошивки мотоциклов. На сайте доступна форма заказа при заполнении которой, отправляется уведомление в Telegram о новом заказе и заказ сохраняется в БД. Стек технологий Django 4, Telegram API, Bootstrap 5.


### Как развернуть проект: :question:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Artem4es/shop.git
```

```
cd shop
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

```
source venv/Scripts/activate (venv/Scripts/activate для Windows)
```

```
python3 -m pip install --upgrade pip (python далее везде для Windows)
```

Установить зависимости из requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate  
```

Создать администратора:
```
python3 manage.py createsuperuser
```

Запустить проект:

```
python3 manage.py runserver
```

## Планы по улучшению проекта: :rocket:

- Добавить защиту от спам рассылок


