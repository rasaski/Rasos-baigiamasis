from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from ckeditor.fields import RichTextField


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class Category(models.Model):
    note_category = models.CharField(max_length=20, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.note_category

    def get_absolute_url(self):
        return reverse('category_list_view')


class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    note = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='foto/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('note_list_view')
