from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("ImageUploader.urls")),
    path('analyze/', include("Analysis.urls")),
]
