from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile_pic(models.Model):
    pic = models.ImageField(upload_to='images')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
