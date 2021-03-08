from django.contrib import admin

from articles.models import Comment, Article


class CommentInLine(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
