from django.shortcuts import render
from django.http import HttpResponse
from .forms import image_input_form
def index(request):
    if request.method == "POST":
        form = image_input_form(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("File uploaded successfully")
        else:
            return HttpResponse("Form is not valid")
    else:
        form  = image_input_form()
    return render(request, "upload/index.html", {"form": form})




# Create your views here.
