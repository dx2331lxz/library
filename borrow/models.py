from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.
class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, to_field='id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    borrow_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(auto_now_add=True)
    is_return = models.BooleanField(default=False)
    is_overdue = models.BooleanField(default=False)
    class Meta:
        db_table = 'borrow'
        verbose_name = '借阅书籍'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book.name