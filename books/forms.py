from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'stock', 'description', 'upc', 'num_reviews']
