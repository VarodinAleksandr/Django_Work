from django.urls import path

from .views import (
    AuthorCreateView,
    AuthorDeleteView,
    AuthorDetailUpdateView,
    AuthorDetailView,
    AuthorList,
    author_detail,
    author_list,
    book_detail, book_list, main_page, publisher_detail, publisher_list, store_detail, store_list
)


app_name = 'library'
urlpatterns = [
    path('', main_page, name='library_main'),
    path('publisher', publisher_list, name='publisher'),
    path('publisher/<int:pk>', publisher_detail, name='publisher_detail'),
    path('author', author_list, name='author'),
    path('author/<int:pk>', author_detail, name='author_detail'),
    path('store', store_list, name='store'),
    path('store/<int:pk>', store_detail, name='store_detail'),
    path('book', book_list, name='book'),
    path('book/<int:pk>', book_detail, name='book_detail'),
    path('author_v2', AuthorList.as_view(), name='author_list_v2'),
    path('author_v2/<int:pk>/', AuthorDetailView.as_view(), name='author_detail_v2'),
    path('author_v2/<int:pk>/update/', AuthorDetailUpdateView.as_view(), name='author_update_v2'),
    path('author_v2/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete_v2'),
    path('author_v2/create/', AuthorCreateView.as_view(), name='author_create_v2'),
]
