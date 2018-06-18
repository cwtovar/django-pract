import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from welcome import database
from welcome/models import PageView

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you want to contact me, foghet about et']})
