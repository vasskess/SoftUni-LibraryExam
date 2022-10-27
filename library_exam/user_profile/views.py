from django.shortcuts import render, redirect

from library_exam.book.models import Book
from library_exam.user_profile.forms import (
    CreateProfileForm,
    EditProfileForm,
    DeleteProfileForm,
)
from library_exam.user_profile.models import Profile


def home(request):
    profile_user = Profile.objects.first()
    books = Book.objects.all()

    rows = []
    per_row = 3

    for i in range(0, len(books), per_row):
        current_row = books[i : i + per_row]
        rows.append(current_row)

    if not profile_user:
        return redirect("register")

    context = {
        "profile_user": profile_user,
        "rows": rows,
    }
    return render(request, "user_profile/home-with-profile.html", context)


def register(request):
    form = CreateProfileForm()
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    books = Book.objects.all()
    context = {"form": form, "books": books}
    return render(request, "user_profile/home-no-profile.html", context)


def profile_page(request):
    profile_user = Profile.objects.first()
    context = {"profile_user": profile_user}
    return render(request, "user_profile/profile.html", context)


def edit_profile(request):
    profile_user = Profile.objects.first()
    form = EditProfileForm(instance=profile_user)
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile_user)
        if form.is_valid():
            form.save()
            return redirect("profile_page")
    context = {"profile_user": profile_user, "form": form}
    return render(request, "user_profile/edit-profile.html", context)


def delete_profile(request):
    profile_user = Profile.objects.get()
    form = DeleteProfileForm(instance=profile_user)
    books = Book.objects.all()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, instance=profile_user)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    context = {"profile_user": profile_user, "form": form}
    return render(request, "user_profile/delete-profile.html", context)
