from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from newsapi import NewsApiClient

from blog_news_portal_project.celery import app
from .models import News, Category


@app.task(bind=True)
def fetch_data(self):
    client = NewsApiClient(api_key=settings.NEWSAPI_API_KEY)
    date_from = timezone.now().date() - timedelta(days=1)
    for category in Category.objects.all():
        response = client.get_everything(q=category.name, language='en', from_param=date_from)
        articles = response.get('articles')
        if articles and len(articles) >= 2:
            article = response.get('articles')[1]
            content = article.get('content').split('[')[0]
            content += f"<a  href='{article.get('url')} target='_blank' class='btn btn-info''>See full article</a>"
            db_article = News(
                source=article['source'].get('name'),
                title=article.get('title'),
                description=content,
                image_url=article.get('urlToImage'),
                category=category,
            )
            db_article.save()

    # print(article.get('author'))
    # print(article.get("title"))
    # print(article.get("content"))

# import requests
# api_key = settings.NEWSAPI_API_KEY
# url = f'https://newsapi.org/v2/everything?q={category}&from={date_form}&sortBy=publishedAt&apiKey={api_key}'
# response = requests.get(url)
# print(response.text)

# to run console
# from news.models import Category
# categories=Category.objects.all()
# from news.utils import fetch_data
# for category in categories:
#     fetch_data(category,"2024-01-01")
