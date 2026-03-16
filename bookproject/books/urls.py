from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:id>/', views.book_detail),

    path('authors/', views.author_list),
    path('authors/<int:id>/', views.author_detail),
]