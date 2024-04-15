"""
URL configuration for bookshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from book.views import hello_view, fun_view, main_view, book_detail_view, book_list_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path("fun/", fun_view),
    path("hello/", hello_view),
    path('', main_view),
    path("books/", book_list_view),
    path("books/<int:book_id>/", book_detail_view),
]
