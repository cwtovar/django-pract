from django.shortcuts import render

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me', 'email@email.com']})
