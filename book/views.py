from django.shortcuts import render, HttpResponse
import datetime
import random
from book.models import Book


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello,its my project.')


def fun_view(request):
    if request.method == 'GET':
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


def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.all()

        context = {'books': books}

        return render(request, 'book/book_list.html', context)


def book_detail_view(request, book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return HttpResponse('Post not found', status=404)

        context = {'book': book}

        return render(request, 'book/book_detail.html', context)



