"""
URL configuration for a blog_news_portal_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views. Home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from news.views import HomePageView, ArticleDetailView, RegisterView, news_likes, CommentsView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', HomePageView.as_view(), name='homepage'),
                  path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
                  path('article/<int:pk>/like', news_likes, name='news_likes'),
                  path('article/<int:pk>/comment', CommentsView.as_view(), name='article_comment'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
                  path('logout/', LogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
