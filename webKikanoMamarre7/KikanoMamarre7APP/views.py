from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>PROGRAMA EN CONSTRUCCION</h1><H2>La Web De Kikano</h2>")