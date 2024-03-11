from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect, render

from main.forms import AuthorForm, BookForm, CategoryForm, ConsumerForm, ReviewForm
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.models import User
from.models import Author, Category, Book, Consumer, Review

@decorators.login_required(login_url='login')
def index(request):
  if request.user.is_staff:
    return render(request, 'admin_page.html')
  else:
    return render(request, 'user_page.html')

def basic_form(request, given_form):
  if request.method == 'POST':
    form = given_form(data=request.POST)
    if form.is_valid():
      form.save()
    else:
      raise Exception(f"some erros {form.errors}")
  return render(request, 'login.html', {'form': given_form()})

def logout_view(request):
  logout(request)
  return render(request, 'logout.html')

def login_view(request):
  if request.method == 'POST':
    form = forms.AuthenticationForm(data=request.POST)
    if form.is_valid():
      try:
        user = authenticate(**form.cleaned_data)
        login(request, user)
        if next := request.GET.get("next"):
          return redirect(next)
        return HttpResponse("OK")
      except Exception:
        return HttpResponse("NOT OK")
    else:
      raise Exception(f"error occured: {form.errors}")
  return render(request, 'login.html', {'form': forms.AuthenticationForm()})


# Get methods
@decorators.login_required(login_url='login')
def get_users(request):
  users = User.objects.all()
  return render(request, 'users.html', {'users': users})

@decorators.login_required(login_url='login')
def get_authors(request):
  authors = Author.objects.all()
  return render(request, 'authors.html', {'authors': authors})

@decorators.login_required(login_url='login')
def get_categories(request):
  if request.method == 'GET':
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
  
@decorators.login_required(login_url='login')
def get_books(request):
  books = Book.objects.all()
  return render(request, 'books.html', {'books': books})

@decorators.login_required(login_url='login')
def get_book(request, id):
  book = Book.objects.get(pk=id)
  if book:
    return render(request, 'book.html', {'book': book})
  else:
    return HttpResponse("Book doesn't exist!")

@decorators.login_required(login_url='login')
def get_consumers(request):
  consumers = Consumer.objects.all()
  return render(request, 'consumers.html', {'consumers': consumers})

@decorators.login_required(login_url='login')
def get_reviews(request):
  sort_by = request.GET.get('sort_by')

  reviews = Review.objects.all()

  if sort_by == 'book':
    reviews = sorted(reviews, key=lambda review: review.book.title)
  elif sort_by == 'user':
    reviews = sorted(reviews, key=lambda review: review.user.username)

  return render(request, 'reviews.html', {'reviews': reviews})

@staff_member_required(login_url='login')
def create_user(request):
  if request.method == 'POST':
    form = forms.UserCreationForm(request.POST)
    try:
      if form.is_valid():
        form.save()
        return redirect('/users')
    except Exception as e:
      print(e)
  else:
    form = forms.UserCreationForm()
  context = {'form': form, 'model': 'user'}
  return render(request, 'form.html', context)

@staff_member_required(login_url='login')
def create_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/categories')
  else:
    form = CategoryForm()
  context = {'form': form, 'model': 'category'}
  return render(request, 'form.html', context)

@staff_member_required(login_url='login')
def create_book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/books')
  else:
    form = BookForm()
  context = {'form': form, 'model': 'book'}
  return render(request, 'form.html', context)

@staff_member_required(login_url='login')
def create_review(request):
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/reviews')
  else:
    form = ReviewForm()
  context = {'form': form, 'model': 'review'}
  return render(request, 'form.html', context)

@staff_member_required(login_url='login')
def create_author(request):
  if request.method == 'POST':
    form = AuthorForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/authors')
  else:
    form = AuthorForm()
  context = {'form': form, 'model': 'author'}
  return render(request, 'form.html', context)

@staff_member_required(login_url='login')
def create_consumer(request):
  if request.method == 'POST':
    form = ConsumerForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/consumers')
  else:
    form = ConsumerForm()
  context = {'form': form, 'model': 'consumer'}
  return render(request, 'form.html', context)