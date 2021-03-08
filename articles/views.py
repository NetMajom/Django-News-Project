from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from articles.models import Article


class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article-list.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article-details.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'content')
    template_name = 'article-update.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    # def dispatch(self, request, *args, **kwargs):
    #     obj = self.get_object()
    #     if obj.szerzo != request.user:
    #         raise PermissionDenied
    #     return super().dispatch(self, request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article-delete.html'
    success_url = reverse_lazy('article-list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article-create.html'
    fields = ('title', 'content')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
