from django.shortcuts import render
from django.http import HttpResponse


def filesys(request):
    return HttpResponse("Filesys App View")