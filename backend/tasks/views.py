from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return HttpResponse('''<h1>Welcome to DevDock!</h1>
                           <h2>These are your tasks.</h2>
                        ''')

