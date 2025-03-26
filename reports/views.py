from django.shortcuts import render
from django.http import HttpResponse


def reports(request, account_name):
    return HttpResponse("Reports App View")