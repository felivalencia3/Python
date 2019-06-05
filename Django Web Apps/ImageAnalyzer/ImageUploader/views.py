from django.shortcuts import render
from django.conf import settings
from .models import ImageInfo
from django.http import HttpResponse
import os
from django.core.files.storage import FileSystemStorage
import cloudinary
import cloudinary.uploader
import cloudinary.api
cloudinary.config(
  cloud_name="felipe-valencia",
  api_key="816872693333612",
  api_secret="piqndQ3cqPaeR6Vcz64UB_Gp7xU"
)

def home(request):
    return render(request, "home.html")
def index(request):
    return render(request, "upload.html")


def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        key = request.POST["key"]
        image = request.FILES['image']
        img_url = cloudinary.uploader.upload(image, public_id=key)["url"]
        imageData = ImageInfo(key=key,url=img_url)
        imageData.save()
        return HttpResponse("Saved to the Cloud and to the Database")
    else:
        return render(request, "upload.html", {
            "acceptedfile": False
        })