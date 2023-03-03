from django.db import models

# Create your models here.

class places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    decc=models.TextField()

    def __str__(self):
        return self.name

class team(models.Model):
    name=models.CharField(max_length=250)
    pic=models.ImageField(upload_to='pics')
    about=models.TextField()

    def __str__(self):
        return self.name
