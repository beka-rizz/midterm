from django.urls import path

from main.views import create_author, create_book, create_category, create_consumer, create_review, create_user, get_authors, get_book, get_books, get_categories, get_consumers, get_reviews, get_users, index, login_view, logout_view

urlpatterns = [
  path('', index, name='index'),
  path('login/', login_view, name='login'),
  # path('register/', register_view, name='register'),
  path("logout/", logout_view, name='logout'),
  
  # Get methods
  path('users/', get_users, name='users'),
  path('authors/', get_authors, name='authors'),
  path('categories/', get_categories, name='categories'),
  path('books/', get_books, name='books'),
  path('books/<int:id>', get_book, name='get_book'),
  path('consumers/', get_consumers, name='consumers'),
  path('reviews/', get_reviews, name='reviews'),
  
  # Post methods
  path('categories/create', create_category, name='create_category'),
  path('authors/create', create_author, name='create_author'),
  path('books/create', create_book, name='create_book'),
  path('reviews/create', create_review, name='create_review'),
  path('consumers/create', create_consumer, name='create_consumer'),
  path('users/create', create_user, name='create_user'),
]