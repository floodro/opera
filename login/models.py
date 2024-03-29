from django.db import models

# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    campus = models.CharField(max_length=200)
    username = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    fullAccess = models.BooleanField(default=True)

    def __str__(self):
        return  f"{self.first_name} {self.last_name}"

class Administrator(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    campus = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return  f"{self.first_name} {self.last_name}"

class Performer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    sr_code = models.CharField(max_length=200)
    campus = models.CharField(max_length=200)
    username = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.sr_code