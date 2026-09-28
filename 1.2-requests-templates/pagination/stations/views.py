import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

STATIONS_PER_PAGE = 10

with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    BUS_STATIONS = list(csv.DictReader(file))


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    paginator = Paginator(BUS_STATIONS, STATIONS_PER_PAGE)
    page = paginator.get_page(request.GET.get('page', 1))

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
