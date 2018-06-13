import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

def storage(request):
    return render(request, 'welcome/view1.html')
