# Readme for News Portal Blog Project

This project is a News Portal Blog built with Django and includes Celery for task scheduling and Eventlet for WebSocket support. The project contains a single app called "news."

## Installation

To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the following dependencies:
- amqp==5.2.0
- asgiref==3.7.2
- billiard==4.2.0
- celery==5.3.6
- certifi==2023.11.17
- charset-normalizer==3.3.2
- click==8.1.7
- click-didyoumean==0.3.0
- click-plugins==1.1.1
- click-repl==0.3.0
- colorama==0.4.6
- cron_descriptor==1.4.0
- Django==5.0.1
- django-celery-beat==2.5.0
- django-celery-results==2.5.1
- django-timezone-field==6.1.0
- dnspython==2.4.2
- eventlet==0.34.2
- greenlet==3.0.3
- idna==3.6
- kombu==5.3.4
- newsapi-python==0.2.7
- pillow==10.2.0
- prompt-toolkit==3.0.43
- python-crontab==3.0.0
- python-dateutil==2.8.2
- redis==5.0.1
- requests==2.31.0
- six==1.16.0
- sqlparse==0.4.4
- tzdata==2023.4
- urllib3==2.1.0
- vine==5.1.0
- wcwidth==0.2.13

## Configuration

The Django settings for the project are defined in `settings.py`. This includes configuration for the database, static files, media files, internationalization, time zone, and more.

## URLs

The URL configuration for the project is defined in `urls.py`. This file contains the URL patterns for routing requests to views.

## Models

The `news` app contains the following models:
- Category
- News
- CommentsModel
- Banner

These models represent categories of news, individual news articles, comments on news articles, and banners for the portal.

## Views

The `news` app contains views for displaying the homepage, article details, user registration, and handling likes and comments on news articles.

## Admin

The admin interface allows management of categories, news articles, comments, and banners.

## Context Processors

A context processor is defined to provide banners for display in templates.

## Forms

Forms are defined for user registration and comments on news articles.

## Tasks

Tasks are defined using Celery for fetching news data from an external API and storing it in the database.

## Additional Information

The project also includes an `__init__.py` file to initialize Celery, and a `tasks.py` file to define Celery tasks.

To run the Celery worker, use the following command:
```bash
celery -A blog_news_portal_project worker -l info
```

To run the Celery beat scheduler, use the following command:
```bash
celery -A blog_news_portal_project beat -l info
```

The project uses Redis as the broker for Celery.

## API Key

The project requires a NewsAPI API key, which is stored in the `settings.py` file as `NEWSAPI_API_KEY`.

Make sure to set up the database and configure the other necessary settings before running the project.

This readme provides an overview of the structure and components of the News Portal Blog project and can serve as a guide for developers working with the project.

For more detailed information on each component, please refer to the respective files and code within the project.

---
This readme provides an overview of the structure and components of the News Portal Blog project and can serve as a guide for developers working with the project.

For more detailed information on each component, please refer to the respective files and code within the project.

If you need further assistance or have any questions about specific components or features of the project, feel free to ask!

![Logo](https://github.com/erfannaderi/daneshkar/blob/main/erfan-high-resolution-logo.png?raw=true)


## Authors

- [@erfannaderi](https://github.com/erfannaderi)


## License

[MIT](https://choosealicense.com/licenses/mit/)



Copyright (c) [2023] [Erfan Naderi]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
 with the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.