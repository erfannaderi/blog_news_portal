from django.contrib import admin

from news.models import Category, News, CommentsModel, Banner


# Register your models here.
@admin.register(Category)
class Admin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    filter_vertical = ()


@admin.register(CommentsModel)
class CommentsModelAdmin(admin.ModelAdmin):
    def check(self, **kwargs):
        return self.checks_class().check(self, **kwargs)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    show_full_result_count = True
