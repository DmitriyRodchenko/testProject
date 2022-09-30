from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, you're at the Classes index.")

# Create your views here.
