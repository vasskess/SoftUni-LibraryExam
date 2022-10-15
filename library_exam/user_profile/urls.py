from django.urls import path
from library_exam.user_profile.views import *


urlpatterns = (
    path("", profile_page, name="profile_page"),
    path("edit/", edit_profile, name="edit_profile"),
    path("delete/", delete_profile, name="delete_profile"),
)
