from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    text = models.TextField(max_length=800)
    number = models.IntegerField()
    positive_num = models.PositiveIntegerField()


# author name, age, active_date, penname, journal

class Author(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    active_date = models.DateField()
    penname = models.CharField(max_length=150)
    journal = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=CASCADE)
    price = models.IntegerField()
    published_date = models.DateField()
    image = models.ImageField(upload_to='uploads', null=False, blank=False)
    book_pdf = models.FileField(upload_to='uploads', null=False, blank=False)
    
    def __str__(self):
        return self.book_name
    
    
# task 
# models task  task name, initial date, deadline, description
# employee name, age, posiiton, department, address, task_assign, photo

