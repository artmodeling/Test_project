# Эта строка стоит в этом файле по умолчанию. Оставить ее без изменений.
from django.contrib import admin

# В этой строке в Джанго из файла store/models.py импортируется модель (класс) Products.
from test_project.models import Products

# В этой строке для Джанго сообщается, что нужно в админке (admin) сайта (site) зарегистрировать (register) модель «Products» (Products).
admin.site.register(Products)
