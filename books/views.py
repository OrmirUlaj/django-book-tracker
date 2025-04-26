from .scraper import scrape_books
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book
from .forms import BookForm

@login_required
def book_list(request):
    if request.user.is_superuser:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(owner=request.user)
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def scrape_books_view(request):
    scrape_books(request.user)
    return redirect('book_list')

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user != book.owner and not request.user.is_superuser:
        return redirect('book_list')

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.user == book.owner or request.user.is_superuser:
        book.delete()

    return redirect('book_list')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'books/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')