from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request):
    print(str(request))
    # return HttpResponse('<h1>Bu home qismi</h1>')
    # kunlar = {"dushanba":("matematika", "fizika", "onatili", "matematika", "fizika", "onatili", "onatili" )}
    return render(request=request, template_name='index.html', context={})
    

def message(request):
    return HttpResponse('<h1>Bu message qismi</h1>')