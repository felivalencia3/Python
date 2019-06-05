from django.urls import path

from . import views

urlpatterns = [
    path('form/', views.index, name='index'),
    path("upload/",views.upload, name="upload"),
    path("",views.home, name="home")
]