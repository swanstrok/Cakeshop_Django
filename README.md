# Euphoria Cakeshop Django
___
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django)

## О проекте:
___
**Euphoria Cakeshop Django** - проект (web-приложение) кондитерской реализованный с помощью Django. 
Вы можете добавить в вашу корзину понравившуюся продукцию. Вы можете добавлять, удалять,
изменять количество товаров в вашей корзине, после чего оформить заказ. В проекте используются
Celery и Redis в качестве брокера сообщений для отправки уведомления на email клиента с 
информацией о заказе. Вся информация о продукции, покупателях, категориях хранится в БД PostgreSQL.
В проекте написаны тесты для тестирования функций с помощью pytest, также реализована концепция 
RESTAPI с помощью Djangorestframework.

### Функционал покупателя:
- возможность выбирать интересующие категории, переход по одиночным страницам конкретного товара;
- совершать одну или несколько покупок добавив товары в корзину и оформив заказ;
- после оформления заказа покупателю придет email-уведомление с информацией о заказе.
Email указывается при оформлении заказа.
- добавление продукции в корзину и дальнейшее оформление заказа доступно только для авторизованных
пользователей.

## Установка зависимостей:
Для работы с проектом в его корне вы можете найти файл с зависимостями 'requirements.txt'.
Установите зависимости для правильной работы проекта с помощью команды:
```python
pip install requirements.txt
```

## Запуск проекта
Для правильного запуска проекта требуется:
- Запустить сервер
```python
python manage.py runserver
```
- Создать новый терминал и запустить в нем Redis
```python
redis-server
```
- Создать новый терминал и запустить в нем Celery
```python
celery -A src worker -l info
```
Для более комфортного отображения выполнения задач Celery в проект установлено приложение flower.
Для его запуска в новом терминале следует прописать:
```python
celery -A src flower
```