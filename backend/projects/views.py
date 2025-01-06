from django.shortcuts import render

from django.http import HttpResponse

def index(reequest):
    return HttpResponse("<h1>Welcome to DevDock!</h1>")
