import email
from django.db import models
from django.contrib.auth.models import User


class Consult(models.Model):
    title=models.CharField(max_length=150)
    text=models.TextField()
    reply=models.TextField(default='')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='conults/',null=True)
    name=models.CharField(max_length=80)
    # email=models.EmailField()
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=1)
    age=models.PositiveIntegerField()
    history=models.TextField()