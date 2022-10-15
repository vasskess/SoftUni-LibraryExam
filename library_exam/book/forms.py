from django.forms import ModelForm

from library_exam.book.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
