from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
   
@login_required
def sitter(request):
    addSitterForm = Sitter_regForm(request.POST)
    message = None
    if request.method == 'POST':
        if addSitterForm.is_valid():
            newSitter = addSitterForm.save(commit = False)
            newSitter.save()
    
        message = "Sitter Added Successfully!"
    
    return render(request, 'dayStarApp/sitter_reg.html', {'addSitterForm': addSitterForm, 'message': message})

@login_required
def baby(request):
    addBabyForm = Baby_regForm()
   
    return render(request, 'dayStarApp/baby_reg.html', {'addBabyForm': addBabyForm}) 

@login_required
def supply(request):
    addSalesForm = Sales_regForm(request.POST)

    message = ""
    if request.method == 'POST':
        if addSalesForm.is_valid():
            message = "Sold item Added Successfully!"
        else:
            message = "Add a correct Item"
        newSalesItem = addSalesForm.save(commit = False)
        newSalesItem.save()
    
    
    return render(request, 'dayStarApp/supply.html', {'addSalesForm': addSalesForm, 'message': message})
    