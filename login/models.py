from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    sr_code = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    cultural_group = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    