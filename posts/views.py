from django.shortcuts import HttpResponse
import datetime
# Create your views here.

def hello_view(requests):
    if requests.method == 'GET':
        return HttpResponse("Hello! Its my project")

def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.date.today())

def good_view(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')