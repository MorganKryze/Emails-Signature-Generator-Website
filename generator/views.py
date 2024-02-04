from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def custom(request):
    return render(request, "custom.html")
