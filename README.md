__Пример реализации логина юзера на джанге, в качестве БД идет постгрес__

Код __взят__ местами частично, местами полностью, все это __демонстрационно_, так как код говно.

Запуск:

1. Ставим python и pip
2. Создаем проект в пайчарме, пишем pip install django, pip install psycopg2, pip install django-crispy-forms
3. python manage.py makemigrations + python manage.py migrate
4. python manage.py createsuperuser
5. python manage.py runserver
6. Переходим на /admin/
7. Логинимся
8. Пробуем зарегать юзера через /register/
9. Получаем ошибку
10. Идем обратно в admin
11. Смотрим таблицу users

Перед всеми этими действиями нужно __настроить базу данных__, например через pgadmin4. Там создаем параметры как в __settings.py__, иначе - меняем его под свои нужды и запускаем так.
