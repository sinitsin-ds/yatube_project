from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=50, verbose_name='имя группы')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='раздел группы')
    description = models.TextField(verbose_name='описание группы')

    def __str__(self):
        return (self.title)

class Post(models.Model):
    text = models.TextField(verbose_name='текст статьи')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='group_posts',
        verbose_name='группа'
    )