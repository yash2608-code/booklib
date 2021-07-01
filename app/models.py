from django.db import models

# Create your models here.
class Seller(models.Model):
    fname = models.CharField(max_length=255,default="Firstname")
    lname = models.CharField(max_length=255,default="Lastname")
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=225,default="Password")

class Category(models.Model):
    Cname = models.CharField(max_length=255,default="Book Category")

    def __str__(self):
        return self.Cname

class Book(models.Model):
    Book_name = models.CharField(max_length=255,default="BookName")
    Author_name = models.CharField(max_length=255,default="Author name")
    Book_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Book_img = models.ImageField(upload_to="bookimages/",default="abc.jpg")
    Book = models.FileField(upload_to="books/",default="book1.pdf")
    BookPrice = models.FloatField(default=0.0)