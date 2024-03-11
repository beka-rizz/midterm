from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField()

  def __str__(self):
    return self.user.username


class Category(models.Model):
  name = models.CharField(max_length=100)

  class Meta:
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name


class Book(models.Model):
  title = models.CharField(max_length=100)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  publication_date = models.DateField()

  def __str__(self):
    return self.title


class Consumer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  books = models.ManyToManyField(Book, related_name='consumers')

  def __str__(self):
    return self.user.username


class Review(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.TextField()
  rating = models.IntegerField()

  def __str__(self):
    return f"{self.user.username}'s review of {self.book.title}"