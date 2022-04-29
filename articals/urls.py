from django.urls import path

from articals.models import Category
from . import views
from .views import HomeView, ArticaleDetail, AddArtical, UpdateArtical, Addcategory, home_view ,CategoryView, DeletArtical, LikeView, CategoryListView
urlpatterns = [
    # path('', views.index, name='index'),
    path('',HomeView.as_view(), name="home"),
    path('articale/<int:pk>', ArticaleDetail.as_view(), name='articale-detail'),
    path('addartical/', AddArtical.as_view(), name='add_Artical'),
    path('addcategory/', Addcategory.as_view(), name='add_category'),
    # path('addartical/', CreateStudentForm)
    path('articale/edit/<int:pk>', UpdateArtical.as_view(), name='edit_Artical'),
    path('articale/<int:pk>/delete', DeletArtical.as_view(), name='delete_Artical'),
    path('test/', home_view, name='test'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    ]
