from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'dayStarApp/index.html')

def sitter(request):
    addSitterForm = Sitter_regForm()
    allSitters = Sitter.objects.all()
    context = {
        'allSitters': allSitters,
    }
    return render(request, 'dayStarApp/sitter.html', {'addSitterForm': addSitterForm})