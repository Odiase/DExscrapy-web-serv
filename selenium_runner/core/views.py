from django.shortcuts import render, HttpResponse
from . import scraping_script2

# Create your views here.
def run_script(request):
    scraping_script2.main()
    return HttpResponse("Running")