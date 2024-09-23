from django.db import models
from Admin.models import *


# Create your models here.
class User_reg(models.Model):
    u_name=models.CharField(max_length=20,default='null')
    User_email=models.CharField(max_length=20)
    user_password=models.CharField(max_length=8)
    u_number=models.IntegerField(default=0)
    u_address=models.CharField(max_length=200,default='null')

class Watch_list(models.Model):
    user_id=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    film_id=models.ForeignKey(Film,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

class User_comment(models.Model):
    film_id=models.ForeignKey(Film,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    user_comment=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
class Like(models.Model):
    user_id=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    film_id=models.ForeignKey(Film,on_delete=models.CASCADE)
    like_count=models.IntegerField(default=0)

class Dislike(models.Model):
    user_id=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    film_id=models.ForeignKey(Film,on_delete=models.CASCADE)
    dislike_count=models.IntegerField(default=0)

class User_subscription(models.Model):
    user_id=models.ForeignKey(User_reg,on_delete=models.CASCADE)
    start_date=models.DateField(auto_now_add=True)
    end_date=models.DateField()
    
