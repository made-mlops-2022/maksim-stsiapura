# Production ready project

## Локальная сборка образа и запуск контейнера
Просто запустите:
~~~
./scripts/run.sh
~~~

## Запуск контейнера из образа на Docker Hub
Для начала следует забрать образ:
~~~
docker pull maksima1ist/online_inference:1.0.2
~~~
И далее запустить его:
~~~
docker run -p 5000:5000 maksima1ist/online_inference:1.0.2
~~~

## Запуск тестов
Внутри контейнера _maksima1ist/online_inference:1.0.2_ необходимо запустить скрипт:
~~~
./scripts/run_test.sh
~~~

## Запросы по REST API
Сперва необходимо установить зависимости:
~~~
pip install pandas==1.5.0 gdown==4.5.3
~~~
Чтобы сделать predict для заранее подготовленных данных (скрипт сам их скачает) запустите:
~~~
python src/predict_data.py
~~~
