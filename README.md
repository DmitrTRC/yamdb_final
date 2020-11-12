![Yamdb-app_workflow](https://github.com/DmitrTRC/yamdb_final/workflows/Yamdb-app_workflow/badge.svg)

# yamdb_final
yamdb_final
Учебный проект от Яндекс.Практикум, представляет собой DRF API приложение базы отзывов о фильмах, книгах и музыке с пройденым код ревью.

##### **Стек технологий:**
* Python3
* Django
* Django REST Framework
* Docker
* Docker-compose

## Build
`docker-compose build`.

## Migrate databases
`docker-compose run --rm web code/manage.py migrate`.

## Run
`docker-compose up`.

##### Подробная документация основана на Redoc и доступна по адресу: <http://127.0.0.1:8020/redoc> после запуска контейнера
