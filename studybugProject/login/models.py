from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_info(models.Model):
    user = models.ForeignKey(User,on_delete=True,null=True,default=1)
    user_interest = models.CharField(max_length=200,null=True)
    #user_img = models.ImageField()

