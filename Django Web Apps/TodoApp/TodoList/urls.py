from django.urls import path
from . import views

app_name = 'TodoApp'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:TodoID>/", views.about, name="about"),
    path("todo/add", views.add, name="addform"),
    path("new", views.new, name="new")
]