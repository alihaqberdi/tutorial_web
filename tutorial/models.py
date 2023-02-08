from django.db.models import Q
from django.db import models
from ckeditor.fields import RichTextField
from django.shortcuts import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tutorial:category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey('Category', related_name='product', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', related_name='product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=550)
    slug = models.SlugField(unique=True)
    discription = RichTextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_activated = models.BooleanField(default=True)

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tutorial:blog_post', args=[self.slug])


class Commentary(models.Model):
    product = models.ForeignKey(Product, related_name='commentary', on_delete=models.CASCADE)
    author = models.ForeignKey('accounts.CustomUser', related_name='commentary', on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=5000)
    is_activated = models.BooleanField(default=True)

    def __str__(self):
        return self.author.username

    class Meta:
        ordering = ('-create',)
        verbose_name_plural = 'Comment'

# class ReplayCommentary(models.Model):
#     comment = models.ForeignKey(Commentary, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
#     create = models.DateTimeField(auto_now_add=True)
#     update = models.DateTimeField(auto_now=True)
#     text = models.CharField(max_length=5000)
#     is_activated = models.BooleanField(default=True)
