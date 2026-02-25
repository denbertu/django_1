from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

from books.models import Book

def home_view(request):
    template = 'base.html'
    return render(request, template)

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
        'pub_date_filter': False
    }
    return render(request, template, context)

def pub_date_view(request, pub_date):
    template = 'books/books_list.html'
    objects = Book.objects.all()
    books = objects.filter(pub_date=pub_date)
    pub_dates = objects.values_list('pub_date')
    pub_dates_list = [d[0].strftime('%Y-%m-%d') for d in pub_dates]
    current_index = pub_dates_list.index(pub_date)
    if current_index == 0:
        prev_page = None
    else:
        prev_page = pub_dates_list[current_index-1]
    if current_index == len(pub_dates_list) - 1:
        next_page = None
    else:
        next_page = pub_dates_list[current_index+1]
    context = {
        'books': books,
        'current_page': current_index,
        'prev_page': prev_page,
        'next_page': next_page,
        'pub_dates': pub_dates_list,
        'pub_date_filter': True
    }
    return render(request, template, context)
