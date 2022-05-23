from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie


def index(request, resource=""):
    return render(request, "index.html")
