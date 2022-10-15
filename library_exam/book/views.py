from django.shortcuts import render, redirect

from library_exam.book.forms import BookForm
from library_exam.book.models import Book
from library_exam.user_profile.models import Profile

profile_user = Profile.objects.first()


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
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
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {"book": book, "form": form, "profile_user": profile_user}
    return render(request, "book/edit-book.html", context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect("home_page")
