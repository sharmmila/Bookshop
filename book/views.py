from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
from book.models import Book
from django.views import View
from django.forms.models import BaseModelForm
from django.views.generic import ListView, DetailView, CreateView

from book.forms import BookForm, BookForm2



def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello, World!')

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')



def fun_view(request):
    if request.method == 'GET':
        memes=('Имя Ибрагим говорит Вам о чем-нибудь?', 'Нталья морская пихота', 'Я сказала стартуем!')
        rand = random.choice(memes)
        return HttpResponse(rand)

class FunView(View):
    def get(self, request):
        memes=('Имя Ибрагим говорит Вам о чем-нибудь?', 'Нталья морская пихота', 'Я сказала стартуем!')
        rand = random.choice(memes)
        return HttpResponse(rand)





def main_view(request):
    mock_data = [
        {

            'title': 'Hello!',
            'datetime': datetime.datetime.now(),

        }
    ]

    if request.method == 'GET':
        return render(request, 'main.html', {'mock_data': mock_data})

class MainView(View):
    template_name = 'main.html'
    mock_data = {'title': 'Hello!', 'datetime': datetime.datetime.now()}
    context = {'mock_data': mock_data}
    def get(self, request):
        return render(request, self.template_name, self.context)


def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()

        context = {'books': books}

        return render(request, 'book/book_list.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'book/book_post_list.html'
    context_object_name = 'books'



def book_detail_view(request, book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return HttpResponse('Post not found', status=404)

        context = {'book': book}

        return render(request, 'book/book_detail.html', context)

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'



def post_create_view(request):
    if request.method == 'GET':
        form = BookForm2()
        return render(request, 'book/book_post_create.html', {'form': form})
    elif request.method == 'POST':
        form = BookForm2(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('book_list_view')

        return render(request, 'book/book_post_create.html', {'form': form})

class PostCreateView(CreateView):
    model = Book
    form_class = BookForm2
    template_name = 'book/book_post_create.html'
    success_url = '/books/'


def review_create_view(request):
    if request.method == 'GET':
        return render(request, 'book/review_create.html',)
    elif request.method == 'POST':
        return redirect('book_detail_view')

    return render(request, 'book/review_create.html', )

class ReviewCreateView(CreateView):
    model = Book
    template_name = 'book/book_review_create.html'
    success_url = '/book_detail/'
