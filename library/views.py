from django.shortcuts import get_object_or_404, render

from .models import Author, Book, Publisher, Store


def publisher_list(request):
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        context = {'publishers': publishers}
    return render(request, 'library/publisher_list.html', context)


def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    context = {'publisher': publisher}
    return render(request, 'library/publisher_detail.html', context)


def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        context = {'authors': authors}
    return render(request, 'library/author_list.html', context)


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    context = {'author': author}
    return render(request, 'library/author_detail.html', context)


def store_list(request):
    if request.method == 'GET':
        stores = Store.objects.all()
        context = {'stores': stores}
    return render(request, 'library/store_list.html', context)


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    context = {
        'store': store,
        'books': store.books.all()
    }
    return render(request, 'library/store_detail.html', context)


def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        context = {'books': books}
    return render(request, 'library/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    authors = book.authors.all()
    context = {
        'book': book,
        'authors': authors,
    }
    return render(request, 'library/book_detail.html', context)
