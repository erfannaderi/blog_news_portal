# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView

from news.forms import NewUserForm, CommentsForm
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
        context['comment_form'] = CommentsForm
        return context


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def news_likes(request, pk):
    news = get_object_or_404(News, pk=pk)
    if news.likes.filter(id=request.user.id).exists():
        news.likes.remove(request.user)
    else:
        news.likes.add(request.user)
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


class CommentsView(FormView):
    form_class = CommentsForm
    # success_url = 'article'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.posted_by = self.request.user
        comment.article = News.objects.get(pk=self.kwargs.get('pk'))
        comment.save()
        return HttpResponseRedirect(reverse('article', args=[self.kwargs.get('pk')]))
