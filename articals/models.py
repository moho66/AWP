from enum import auto
from django.db import models
from mysite.settings import BASE_DIR
from django.contrib.auth.models import User
from django.urls import reverse
# from .models import AddArticalForm
class Artical(models.Model):
    title = models.CharField(max_length=50)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)  #if we delete user all the post we be deleted
    text= models.TextField()
    views= models.IntegerField(default=0)
    Date=models.DateField()
    img=models.FileField(upload_to=BASE_DIR.joinpath("photo"), default="")

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


