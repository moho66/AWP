from cgitb import text
import imp
from multiprocessing import context
from pdb import post_mortem
from re import A, template
from unicodedata import category
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
import articals
from articals.models import Artical
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django import forms
from .forms import AddArticalForm, InputForm, UpdateArtical
from .models import Artical, Category
from django.db.models import F
from django.urls import reverse_lazy, reverse
from mysite.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
def LikeView(request, pk):
    post = get_object_or_404(Artical, id=request.POST.get('post_id'))
    post.Likes.add(request.user)
    return HttpResponseRedirect(reverse('articale-detail', args=[str(pk)]))
# def index(request):
#     articals=Artical.objects.all()
#     context={'articals':articals}
#     return render(request, "index.html",context)

class HomeView(ListView):
    model = Artical
    template_name = 'index.html'
    ordering =['-views']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context

class ArticaleDetail(DetailView):
    model = Artical
    template_name = 'article_details.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticaleDetail, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Artical, id=self.kwargs['pk'])
        total_Likes = stuff.total_Likes()
        context["cat_menu"] = cat_menu
        context["total_Likes"] = total_Likes
        
        return context

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
    def post(self, request, *args, **kwargs):
        art=Artical.objects.create(title=request.POST['title'],text=request.POST['text'],category=request.POST['category'],author=request.user)
        fs=FileSystemStorage(MEDIA_ROOT.joinpath('photo'))
        fn=fs.generate_filename(request.FILES['img'].name)
        fs.save(fn,request.FILES['img'])
        art.img.name='photo/'+fn
        art.save()
        return redirect('home')
class DeletArtical(DeleteView):
    model = Artical
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class Addcategory(CreateView):
    model = Category
    #form_class = AddArticalForm
    template_name = 'add_category.html'
    fields = '__all__'
    #fields = ('title', 'text')

class UpdateArtical(UpdateView):
    model = Artical
    form_class = UpdateArtical
    template_name = 'update_post.html'
    # fields = ('title', 'text', 'img', 'date')


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Artical.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})
    
    


def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "test.html", context)

# def CreateStudentForm(request):
#     form = AddArticalForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         context = {
#         'form' : form
#     }

#     return render(request, 'add_post.html', context)