from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request,"core/index.html")
