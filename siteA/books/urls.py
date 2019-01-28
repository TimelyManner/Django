from django.urls import path
from books import views 

app_name = 'books'
 
urlpatterns = [
    path('', views.BooksModelView.as_view(), name='index'),        
    path('book/', views.BooksModelView.as_view(), name='book_list'),
    path('author/', views.BooksModelView.as_view(), name='author_list'),
    path('publisher/', views.BooksModelView.as_view(), name='publisher_list'),    
]