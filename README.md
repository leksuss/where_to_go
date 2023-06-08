# Where To Go

This site is for Moscow tourists and Moscow citizens. It shows interesting places with foto and description on Moscow map. This is the source code of site. Working site you can see here:
http://leksus.pythonanywhere.com/.

Admin panel located here: http://leksus.pythonanywhere.com/admin/.

## How to install

### Requirements

 - python3.6+
 - `django`
 - `pillow`
 - `django-admin-sortable2`
 - `django-tinymce`
 - `environs`
 - `requests`

### How to setup and run

Get the source code of this repo:
```
git clone https://github.com/leksuss/where_to_go.git
```

Go to this script:
```
cd where_to_go
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

Set environment variables in `.env` file. Repo has an example of this file `.env_example`, so you can rename it: 
```
mv .env_example .env
```
and fill with necessary data:
 - `SECRET_KEY`, random string at least 50 characters
 - `DEBUG`, set it to `False` if you will run it in production otherwize `True`
 - `ALLOWED_HOSTS`, comma-separated list of hosts. `127.0.0.1` for local development or your host(domain name) for production 

Then run migrations:
```
python3 manage.py migrate
```

To login in admin panel you should create user, use this command and follow instructions:
```
python3 manage.py createsuperuser
```

Run Django built-in webserver:
```
python3 manage.py runserver
```

And then open your favorite browser and type in the address bar this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/), admin panel located here: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


## How to fill site with data examples

Go [here](https://github.com/devmanorg/where-to-go-places/tree/master/places), this is a list of json files with data of each place. To add place in site, run:

```
python3 manage.py load_place <url_to_json>
```

Of course, you can create your own json file with the place data. Here is example of the it's structure:
```json
{
    "title": "Антикафе Bizone",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1f09226ae0edf23d20708b4fcc498ffd.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/6e1c15fd7723e04e73985486c441e061.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/be067a44fb19342c562e9ffd815c4215.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/f6148bf3acf5328347f2762a1a674620.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b896253e3b4f092cff47a02885450b5c.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/605da4a5bc8fd9a748526bef3b02120f.jpg"
    ],
    "description_short": "Настольные и компьютерные игры, виртуальная реальность и насыщенная программа мероприятий — новое антикафе Bizone предлагает два уровня удовольствий для вашего уединённого отдыха или радостных встреч с родными, друзьями, коллегами.",
    "description_long": "<p>Рядом со станцией метро «Войковская» открылось антикафе Bizone, в котором создание качественного отдыха стало делом жизни для всей команды. Создатели разделили пространство на две зоны, одна из которых доступна для всех посетителей, вторая — только для совершеннолетних гостей.</p><p>В Bizone вы платите исключительно за время посещения. В стоимость уже включены напитки, сладкие угощения, библиотека комиксов, большая коллекция популярных настольных и видеоигр. Также вы можете арендовать ВИП-зал для большой компании и погрузиться в мир виртуальной реальности с помощью специальных очков от топового производителя.</p><p>В течение недели организаторы проводят разнообразные встречи для меломанов и киноманов. Также можно присоединиться к английскому разговорному клубу или посетить образовательные лекции и мастер-классы. Летом организаторы запускают марафон настольных игр. Каждый день единомышленники собираются, чтобы порубиться в «Мафию», «Имаджинариум», Codenames, «Манчкин», Ticket to ride, «БЭНГ!» или «Колонизаторов». Точное расписание игр ищите в группе антикафе <a class=\"external-link\" href=\"https://vk.com/anticafebizone\" target=\"_blank\">«ВКонтакте»</a>.</p><p>Узнать больше об антикафе Bizone и забронировать стол вы можете <a class=\"external-link\" href=\"http://vbizone.ru/\" target=\"_blank\">на сайте</a> и <a class=\"external-link\" href=\"https://www.instagram.com/anticafe.bi.zone/\" target=\"_blank\">в Instagram</a>.</p>",
    "coordinates": {
        "lng": "37.50169",
        "lat": "55.816591"
    }
}
```

## Data source
All data is from [kudago.com](http://kudago.com)

## Goals
This project is made for study purpose.
