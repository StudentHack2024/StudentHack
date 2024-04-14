from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


urlpatterns = [path("", views.index, name = "index")]

urlpatterns += staticfiles_urlpatterns()