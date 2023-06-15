from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("", include("questions.urls")),
    path("", include("student.urls")),
    path("", include("teacher.urls")),
]
