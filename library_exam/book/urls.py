from django.urls import path
from library_exam.book.views import *

urlpatterns = (
    path("", add_book, name="add_book"),
    path("edit<str:pk>/", edit_book, name="edit_book"),
    path("details<str:pk>/", book_details, name="book_details"),
    path("delete<str:pk>/", delete_book, name="delete_book"),
)
