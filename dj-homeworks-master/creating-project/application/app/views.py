import csv
import os
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


CSV_FILENAME = 'phones.csv'
COLUMNS = [
    {'name': 'id', 'width': 1},
    {'name': 'name', 'width': 3},
    {'name': 'price', 'width': 2},
    {'name': 'release_date', 'width': 2},
    {'name': 'lte_exists', 'width': 1},
]


def table_view(request):
    template = 'table.html'
    with open(CSV_FILENAME, 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': COLUMNS, 
            'table': table, 
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result


def home_view(request):
    pages = ['admin/', 'table/', 'home/', 'current_time/', 'workdir/']
    return HttpResponse('\n'.join(pages))


def time_view(request):
    time_now = datetime.today().strftime("%H:%M:%S")
    return HttpResponse(time_now)


def workdir_view(request):
    workdir = os.listdir()
    return HttpResponse('\n'.join(workdir))


