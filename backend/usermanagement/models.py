from django.db import models

# Create your models here.
class User(models.Model):
    #adding fields to the
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    username = models.CharField(unique = True, max_length = 20, null=False ,default=True)
    password1 = models.CharField(max_length = 15, null=False,blank = False)
    password2 = models.CharField(max_length = 15, null = False, blank = False)
