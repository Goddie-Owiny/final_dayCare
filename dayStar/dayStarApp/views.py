from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.template import loader

# Create your views here.
def index(request):
    all_sitters = Sitter.objects.all()
    all_babys = Baby.objects.all()
    count_sitters = Sitter.objects.count()
    count_babys = Baby.objects.count()
    context = {
        'count_sitters': count_sitters,
        'count_babys': count_babys,
        'all_sitters': all_sitters,
        'all_babys': all_babys,
    }
    template = loader.get_template('dayStarApp/index.html')
    return HttpResponse(template.render(context))

def landing(request):
    return render(request, 'dayStarApp/landing.html')
   

def sitter(request):
    addSitterForm = Sitter_regForm(request.POST)
    message = None
    if request.method == 'POST':
        if addSitterForm.is_valid():
            newSitter = addSitterForm.save(commit = False)
            newSitter.save()
    
    message = "Sitter Added Successfully!"
    
    

    return render(request, 'dayStarApp/sitter_reg.html', {'addSitterForm': addSitterForm, 'message': message})


def baby(request):
    addBabyForm = Baby_regForm()
   
    return render(request, 'dayStarApp/baby_reg.html', {'addBabyForm': addBabyForm}) 
    