from django.contrib import admin
from django.urls import path, include

from library_exam.user_profile.views import *

urlpatterns = (
    path("admin/", admin.site.urls),
    path("", home, name="home_page"),
    path("create/", register, name="register"),
    path("profile/", include("library_exam.user_profile.urls")),
    path("book/", include("library_exam.book.urls")),
)
