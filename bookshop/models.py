from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=256)
    language = models.CharField(default='English', max_length=265)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=265)
    author = models.ForeignKey(Author(), on_delete=models.CASCADE)
    publish_date = models.DateField()
    isbn = models.IntegerField()
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])
