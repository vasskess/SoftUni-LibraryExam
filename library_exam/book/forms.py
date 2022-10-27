from django.forms import ModelForm
from django import forms
from library_exam.book.models import Book


class BaseBookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "title": forms.TextInput({"placeholder": "Title"}),
            "description": forms.Textarea({"placeholder": "Description"}),
            "image": forms.URLInput({"placeholder": "Image"}),
            "type": forms.TextInput({"placeholder": "Fiction, Novel, Crime..."}),
        }


class CreateBookForm(BaseBookForm):
    pass


class EditBookForm(BaseBookForm):
    pass


class DeleteBookForm(BaseBookForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
