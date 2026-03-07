from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField()
    articles = models.ManyToManyField(Article, related_name='tags', through='Scope')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Scope(models.Model):
    tag = models.ForeignKey(Tag, related_name='scopes', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='scopes', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_main', '-tag']