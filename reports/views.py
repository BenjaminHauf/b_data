from django.shortcuts import render
from django.http import HttpResponse


def reports(request):
    return HttpResponse("Reports App View")