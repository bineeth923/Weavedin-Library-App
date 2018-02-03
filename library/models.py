from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=6)
    year = models.DateField
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def fun(self):
        return self.age


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=10)
    description = models.CharField(max_length=3000)

    def __str__(self):
        return self.name
