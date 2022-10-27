from django.shortcuts import render, redirect

from library_exam.book.forms import CreateBookForm, EditBookForm, DeleteBookForm
from library_exam.book.models import Book
from library_exam.user_profile.models import Profile

profile_user = Profile.objects.first()


def add_book(request):
    form = CreateBookForm()
    if request.method == "POST":
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {"form": form, "profile_user": profile_user}
    return render(request, "book/add-book.html", context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {"book": book, "profile_user": profile_user}
    return render(request, "book/book-details.html", context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = EditBookForm(instance=book)

    if request.method == "POST":
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_details", pk)
    context = {"book": book, "form": form, "profile_user": profile_user}
    return render(request, "book/edit-book.html", context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    form = DeleteBookForm(instance=book)
    form.save()
    return redirect("home_page")
