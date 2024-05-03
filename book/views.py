from django.shortcuts import render, HttpResponse, redirect
import datetime
import random
from book.models import Book
from typing import Any
from django.views import View
from django.forms.models import BaseModelForm
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView

from book.forms import BookForm, BookForm2, SearchForm



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
        search = request.GET.get('search')  # None
        tags = request.GET.getlist('tags')  # [id`1, id`2, id`3]
        ordering = request.GET.get('ordering')  # 'title'
        page = int(request.GET.get('page', 1))  # 1

        search_form = SearchForm(request.GET)
        posts = Book.objects.all().select_related('author').prefetch_related('tags').prefetch_related('categories')
        # SELECT * FROM post_post JOIN auth_user ON post_post.author_id = auth_user.id

        if search:
            posts = posts.filter(
                Q(title__icontains=search) | Q(text__icontains=search)
            )
        if tags:
            posts = posts.filter(tags__id__in=tags).distinct()

        if ordering:
            posts = posts.order_by(ordering)

        limit = 4
        max_pages = posts.count() / limit

        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page * limit

        posts = posts[start:end]

        context = {'posts': posts, 'name': "Esen", 'search_form': search_form, 'max_pages': range(1, max_pages + 1)}

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
            # form.save()
            Book.objects.create_post(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                image=form.cleaned_data['image'],
                # author=request.user
            )

            return redirect('book_list_view')

        return render(request, 'book/book_post_create.html', {'form': form})

class PostCreateView(CreateView):
    model = Book
    form_class = BookForm2
    template_name = 'book/book_post_create.html'
    success_url = '/books/'


def get(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('login_view')
    form = self.get_form()
    return self.render_to_response({'form': form})


def form_valid(self, form: BaseModelForm) -> Any:
    form.instance.author = self.request.user
    self.object = form.save()
    return redirect(self.get_success_url())

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
