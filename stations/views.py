import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def get_csv_file_content(file_name, encoding):
    content = []
    with open(file_name, encoding=encoding) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content.append(
                {
                    'Name': row['Name'],
                    'Street': row['Street'],
                    'District': row['District']
                }
            )
    return content


def bus_stations(request):
    content = get_csv_file_content(BUS_STATION_CSV, 'utf-8')
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
