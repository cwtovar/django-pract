import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from welcome import database
from .models import PageView

def index(request):
    return render(request, 'welcome/index.html')
