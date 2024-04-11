from django.shortcuts import render, HttpResponse
import datetime
import random


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



