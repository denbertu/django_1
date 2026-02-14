from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))

data = settings.BUS_STATION_CSV

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(data, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        bus_stations = list(csv_reader)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(bus_stations, 10)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page
        }
        return render(request, 'stations/index.html', context)
