from django import forms
from .models import Category, Book

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('category_id', 'name','author', 'description', 'price', 'file', 'image')
