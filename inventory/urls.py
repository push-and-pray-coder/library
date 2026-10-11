from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='inventory_page'),
    path('add/', views.AddBookView.as_view(), name='add_book'),
    path('edit/<int:pk>/', views.EditBookView.as_view(), name='edit_book'),
    path('delete/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book'),
]