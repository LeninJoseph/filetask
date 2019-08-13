from django.urls import path
from . import views



urlpatterns = [
    path('', views.login, name='login'),
    path('home/',views.index, name='index'),
    path('receive/',views.receive, name='receive'),
    path('upload/',views.upload,name='upload'), 
    path('success/',views.success,name='success'),
    path('uploader/', views.uploader, name='uploader'),
    path('upload_history/', views.upload_history, name='upload_history'),
    path('logout/',views.logout, name='logout'),   
]
