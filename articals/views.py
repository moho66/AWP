from cgitb import text
import imp
from pdb import post_mortem
from re import A, template
from django.shortcuts import render
from django.http import HttpResponse
import articals
from articals.models import Artical
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from .forms import AddArticalForm
from .models import Artical
from django.db.models import F

# def index(request):
#     articals=Artical.objects.all()
#     context={'articals':articals}
#     return render(request, "index.html",context)

class HomeView(ListView):
    model = Artical
    template_name = 'index.html'

class ArticaleDetail(DetailView):
    model = Artical
    template_name = 'article_details.html'
    def get(self, request, pk):
        artical = Artical.objects.get(pk=pk)
        artical.views = F("views")+1
        artical.save()
        return super().get(request)
    
class AddArtical(CreateView):
    model = Artical
    form_class = AddArticalForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #fields = ('title', 'text')

class UpdateArtical(UpdateView):
    model = Artical
    form_class = AddArticalForm
    template_name = 'update_post.html'
    # fields = ('title', 'text', 'img', 'date')


# def CreateStudentForm(request):
#     form = AddArticalForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         context = {
#         'form' : form
#     }

#     return render(request, 'add_post.html', context)