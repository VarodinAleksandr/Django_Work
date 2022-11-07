from django.urls import path

from .views import (
    author_detail,
    author_list,
    book_detail,
    book_list,
    publisher_detail,
    publisher_list,
    store_detail,
    store_list
)


app_name = 'library'
urlpatterns = [
    path('publisher', publisher_list, name='publisher'),
    path('publisher/<int:pk>', publisher_detail, name='publisher_detail'),
    path('author', author_list, name='author'),
    path('author/<int:pk>', author_detail, name='author_detail'),
    path('store', store_list, name='store'),
    path('store/<int:pk>', store_detail, name='store_detail'),
    path('book', book_list, name='book'),
    path('book/<int:pk>', book_detail, name='book_detail'),
]
