from django.urls import path
from . import views
from .views import HomeView, ArticaleDetail, AddArtical, UpdateArtical
urlpatterns = [
    # path('', views.index, name='index'),
    path('',HomeView.as_view(), name="home"),
    path('articale/<int:pk>', ArticaleDetail.as_view(), name='articale-detail'),
    path('addartical/', AddArtical.as_view(), name='add_Artical'),
    # path('addartical/', CreateStudentForm)
    path('articale/edit/<int:pk>', UpdateArtical.as_view(), name='edit_Artical'),
    ]
