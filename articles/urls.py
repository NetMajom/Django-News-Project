from django.urls import path

from articles.views import ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView, ArticlesListView

urlpatterns = [
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-details'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('', ArticlesListView.as_view(), name='article-list')
]
