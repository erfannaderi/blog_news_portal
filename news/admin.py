from django.contrib import admin

from news.models import Category, News


# Register your models here.
@admin.register(Category)
class Admin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    filter_vertical = ()
