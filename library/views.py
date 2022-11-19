from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg, Count
from django.db.models.functions import Round
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic

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


class AuthorList(generic.ListView):
    model = Author
    template_name = 'library/author_list_v2.html'
    paginate_by = 5


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
