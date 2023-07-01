from datetime import date
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now 


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=255, default="super project")
    date = models.DateField(default=now)
    link = models.TextField(default="this is nigeria")
    content = models.TextField(default="this is nigeria")
    description = models.TextField(default="this is nigeria")
    owner = models.ForeignKey(to=User, on_delete = models.CASCADE)
    category = models.CharField(max_length=255, default="super project")
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    image1 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='static/images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date']



class Category(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(to=User, on_delete = models.CASCADE)
    
    
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    
    def __str__(self):
        return self.name
    

class Certificate(models.Model):
    name = models.CharField(max_length=100, default="this is nigeria")
    pdf = models.FileField(upload_to='static/pdfs/', null=True, blank=True)
    cover = models.ImageField(upload_to='static/images/', null=True, blank=True)
    
        
    
    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
        
        
        
class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    twitter_handle = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email
    
class Reviews(models.Model):
    name = models.CharField(max_length=100, default="this is nigeria")
    cover = models.ImageField(upload_to='static/images/', null=True, blank=True)

    def __str__(self):
        return self.name
        

    
        
