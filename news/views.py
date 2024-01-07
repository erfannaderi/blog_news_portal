# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from news.forms import NewUserForm
from news.models import News


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['News'] = News.objects.all().order_by('-created_at')
        return context


class ArticleDetailView(TemplateView):
    template_name = 'article_details.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article'] = News.objects.get(pk=kwargs.get('pk'))
        return context


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
