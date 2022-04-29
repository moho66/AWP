from enum import auto
from logging import PlaceHolder
from unicodedata import category
from django.db import models
from mysite.settings import BASE_DIR
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
# from .models import AddArticalForm

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        #return reverse('articale-detail', kwargs={'pk' : self.pk})
        return reverse('home')

   



class Artical(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=255, default='coding')
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, default="username")  #if we delete user all the post we be deleted
    text= models.TextField()
    views= models.IntegerField(default=0)
    Date=models.DateField(auto_now_add=True)
    img=models.FileField(upload_to=BASE_DIR.joinpath("photo"), default="")
    Likes=models.ManyToManyField(User, related_name='blog_posts')


    def total_Likes(self):
        return self.Likes.count()

    def get_absolute_url(self):
        #return reverse('articale-detail', kwargs={'pk' : self.pk})
        return reverse('home')
    def __str__(self):
        return self.title + ' | ' + str(self.author) #show title and author in strange number
        
    # def imagetest(request):  
    #     form=AddArticalForm()
    #     if request.method=='POST':

    #         form = AddArticalForm(request.POST, request.FILES)
    #         if form.is_valid():
    #                 form.save()
    #               img = form.cleaned_data['img']
    #               p=Artical(Comments=Comments,img=img)
    #               p.save()

    #     return render(request,'home.html',{'form':form,'up':upload.objects.all(), })


# def get_absolute_url(self):
#     return reverse('articale-detail', args=(str(self.id)))


