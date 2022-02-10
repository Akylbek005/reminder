# Reminder

## Как запустить проэкт

> Перед запуском у вас должен быть установлен python 3.8 и git 

### В терминале пишем эти команды
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
#### После этих комманд сервер будет доступен по адресу http://127.0.0.1:8000

---------------------------------------------------

#### Запустить отправку email 
```bash
python manage.py crontab add
```
Выйдет хеш похожий на этот `161efb8efccfcd66489829bc358a7807` и отпрака email будет рабоать.

Но что бы протестировть отправку добавьте в базу данных данные с birthday на 7 дней вперед.

И запустите команду:
```bash
python manage.py crontab run <hash>
```
В нашем случае <hash> это `161efb8efccfcd66489829bc358a7807`
