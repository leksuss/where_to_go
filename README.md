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
Run Django built-in webserver:
```
python3 manage.py runserver
```

And then open your favorite browser and type in the address bar this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## How to fill site with data examples

Go [here](https://github.com/devmanorg/where-to-go-places/tree/master/places), this is a list of json files with data of each place. To add place in site, run:

```
python3 manage.py <url_to_json>
```

## Data source
All data is from http://kudago.ru

## Goals
This project is made for study purpose.
