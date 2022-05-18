# Api_yatube
## _Программа для работы с Api поекта Yatube_


## Установка

Скачайте репозиторий 

```sh
git clone 
```

Установите виртуальное окружение 

```sh
python3 -m venv venv 
```
Установите все нужные пакеты 

```sh
pip install -r requirements.txt
```

Запустите приложени

```sh
python3 manage.py runserver
```
## Работа с приложением 
Получите токен пользователя
```
http://127.0.0.1:8000/api/v1/api-token-auth/
{
    "username":"",
    "password":""
}
```