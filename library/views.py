from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import InvalidPage
from django.db.models import Avg, Count
from django.db.models.functions import Round
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page

from .forms import AuthorForm
from .models import Author, Book, Publisher, Store


def main_page(request):
    if request.method == 'GET':
        return render(request, 'library/main_page.html')


def publisher_list(request):
    if request.method == 'GET':
        publishers = Publisher.objects.prefetch_related('books').annotate(number_of_books=Count('books')).all()
        context = {'publishers': publishers}
        return render(request, 'library/publisher_list.html', context)


def publisher_detail(request, pk):
    if request.method == 'GET':
        publisher = get_object_or_404(Publisher, pk=pk)
        context = {'publisher': publisher}
        return render(request, 'library/publisher_detail.html', context)


def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.prefetch_related('books').annotate(number_of_books=Count(
            'books'), avg_rating=Round(Avg('books__rating'), precision=2)).all()
        context = {'authors': authors}
        return render(request, 'library/author_list.html', context)


def author_detail(request, pk):
    if request.method == 'GET':
        author = get_object_or_404(Author, pk=pk)
        context = {'author': author}
        return render(request, 'library/author_detail.html', context)


def store_list(request):
    if request.method == 'GET':
        stores = Store.objects.prefetch_related('books').annotate(number_of_books=Count('books')).all()
        context = {'stores': stores}
        return render(request, 'library/store_list.html', context)


def store_detail(request, pk):
    if request.method == 'GET':
        store = get_object_or_404(Store.objects.prefetch_related('books'), pk=pk)
        context = {
            'store': store,
            'books': store.books.all()
        }
        return render(request, 'library/store_detail.html', context)


def book_list(request):
    if request.method == 'GET':
        books = Book.objects.select_related('publisher').prefetch_related(
            'authors').annotate(number_of_authors=Count('authors'), rounded_rating=Round('rating', precision=2)).all()
        context = {'books': books}
        return render(request, 'library/book_list.html', context)


def book_detail(request, pk):
    if request.method == 'GET':
        book = get_object_or_404(Book.objects.select_related('publisher').prefetch_related('authors'), pk=pk)
        authors = book.authors.all()
        context = {
            'book': book,
            'authors': authors,
        }
        return render(request, 'library/book_detail.html', context)


@method_decorator(cache_page(10), 'dispatch')
class AuthorList(generic.ListView):
    model = Author
    template_name = 'library/author_list_v2.html'
    paginate_by = 20

    def get_queryset(self):
        authors = Author.objects.prefetch_related('books').annotate(number_of_books=Count(
            'books'), avg_rating=Round(Avg('books__rating'), precision=2), store_number=Count('books')).all()
        return authors

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset,
            page_size,
            orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty(),
        )
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == "last":
                page_number = paginator.num_pages
            else:
                raise Http404("Page is not “last”, nor can it be converted to an int.")
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage:
            page = paginator.page(1)
            return (paginator, page, page.object_list, page.has_other_pages())


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'library/author_detail_v2.html'
    context_object_name = 'author'


class AuthorDetailUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    template_name = 'library/author_update.html'
    form_class = AuthorForm
    login_url = '/admin/login/'

    def get_success_url(self):
        return reverse_lazy('library:author_detail_v2', kwargs={'pk': self.object.pk})


class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    http_method_names = ['delete', 'post', 'get']
    model = Author
    success_url = reverse_lazy('library:author_list_v2')
    template_name = 'library/delete_author_v2.html'
    login_url = '/admin/login/'


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    template_name = 'library/author_create_v2.html'
    form_class = AuthorForm
    login_url = '/admin/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('library:author_detail_v2', kwargs={'pk': self.object.pk})
