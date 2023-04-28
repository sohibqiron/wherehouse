from pickle import NONE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models 
from stockapp.models import Warehouse
from .managers import StockUserManager
# Create your models here.

class StockUser(AbstractUser):
    username = None 
    email = models.EmailField(verbose_name='Email Adress',max_length=255,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StockUserManager()

    def __str__(self):
        return self.email 


class Profile(models.Model):
    LEVEL_CHOICES = [
        ('Director','Director'),
        ('Manager','Manager'),
        ('Direver','Driver'),
        ('Worker','Worker'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    level = models.CharField(max_length=9,choices=LEVEL_CHOICES,default='Worker')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    warehouse = models.ForeignKey(Warehouse,on_delete=models.SET_NULL,null=True)
    is_approved = models.BooleanField(verbose_name="Approve user",default=False)

    def __str__(self):
        return f"{self.level} {self.first_name} {self.last_name}"



