from django.urls import path, include
from api_bookstore import views

urlpatterns = [
    path('authors/', views.author_list),
    path('authors/<int:pk>/', views.author_detail),
    path('books/', views.books_list),
    path('authors/<int:pk>/', views.book_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]