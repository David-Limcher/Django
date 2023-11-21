from django.shortcuts import render
from django.http import HttpResponse
from .forms import YourForm

def home(request):
    return render(request, 'app_name/home.html')

def form_page(request):
    form = YourForm()
    return render(request, 'app_name/form_page.html', {'form': form})