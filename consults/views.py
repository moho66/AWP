from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from consults.models import *
from mysite.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage

def sendDconsult(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        if request.method=='POST':
            consult=Consult() 
            consult.title=request.POST['title']
            consult.text=request.POST['text']
            consult.user=request.user
            consult.name=request.POST['name']
            consult.phone=request.POST['phone']
            consult.age=request.POST['age']
            consult.history=request.POST['histroy']
            consult.gender=request.POST['gender']
            if 'img' in request.FILES:   
                fs=FileSystemStorage(MEDIA_ROOT.joinpath('consults'))
                fn=fs.generate_filename(request.FILES['img'].name)
                fs.save(fn,request.FILES['img'])
                consult.img.name='consults/'+fn
            consult.save()
        return render(request,'send_consult.html')
    else:
        return redirect('home')

def myConsults(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        if  request.user.is_superuser:
            consutls=Consult.objects.all()
        else:
            consutls=Consult.objects.filter(user=request.user)
        contxt={'consutls':consutls}
        return render(request,'consults.html',context=contxt)
    else:
       return  redirect('home')

def setConsultReply(request,id):
    if request.user.is_authenticated and not request.user.is_anonymous and  request.user.is_superuser:
            cons=get_object_or_404(Consult,pk=id)
            cons.reply=request.POST['text']
            cons.save()
            return redirect(reverse('consult',kwargs={'id':id}))
    else:
            return redirect('home')


def consult(request,id):
    con=Consult.objects.get(pk=id)
    return render(request,'consult.html',{"con":con})