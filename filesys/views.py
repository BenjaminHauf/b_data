from django.shortcuts import render
from django.http import HttpResponse


def filesys(request, account_name):
    return HttpResponse("Filesys App View")