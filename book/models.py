from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    author = models.CharField(max_length=32)
    publish = models.CharField(max_length=32)
    pub_date = models.DateField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "书籍"
        verbose_name_plural = "书籍"