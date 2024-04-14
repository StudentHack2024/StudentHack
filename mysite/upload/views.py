from django.shortcuts import render
from django.http import HttpResponse
from .forms import image_input_form
from.services.classify import classify_img
import base64

def index(request):
    if request.method == "POST":
        form = image_input_form(request.POST, request.FILES)
        if form.is_valid():
            prediction = classify_img(request.FILES['image'])
            img_str = base64.b64encode(request.FILES['image'].file.getvalue())
            print(request.FILES['image'].read())
            img_str = img_str.decode("utf-8")
            return render(request, "upload/classified_page.html", {"prediction": prediction, "image_b64": img_str})
        else:
            return render(request, "upload/oops.html")
    else:
        form  = image_input_form()
    return render(request, "upload/index.html", {"form": form})

def index2(request):
    if request.method == "POST":
        form = image_input_form(request.POST, request.FILES)
        if form.is_valid():
            prediction = classify_img(request.FILES['image'])
            img_str = base64.b64encode(request.FILES['image'].file.getvalue())
            img_str = img_str.decode("utf-8")
            return render(request, "upload/classified_page.html", {"prediction": prediction, "image_b64": img_str})
        else:
            return render(request, "upload/oops.html")
    else:
        form  = image_input_form()
    return render(request, "upload/index2.html", {"form": form})

