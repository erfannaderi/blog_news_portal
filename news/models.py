from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    likes = models.ManyToManyField(get_user_model(), related_name='news_likes')

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return f"{self.title} created by {self.created_by}"

    def number_of_likes(self):
        return self.likes.count


class CommentsModel(models.Model):
    article = models.ForeignKey(News, on_delete=models.PROTECT)
    posted_by = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    post_date = models.DateTimeField(blank=True, null=True,auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-post_date']

    def __str__(self):
        return f'{self.article.__str__()} {self.comment} by : {self.posted_by.get_full_name()}'


class Banner(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField()
    url = models.URLField(blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return self.name
