from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from datetime import datetime


# Create your views here.
@login_required
def index(request):
    all_sitters = Sitter.objects.all()
    all_babys = Baby.objects.all()
    count_sitters = Sitter.objects.count()
    count_babys = Baby.objects.count()
    # all_sale = Sale.objects.all()
    context = {
        'count_sitters': count_sitters,
        'count_babys': count_babys,
        'all_sitters': all_sitters,
        'all_babys': all_babys,
        # 'all_sale': all_sale,
    }
    template = loader.get_template('dayStarApp/index.html')
    return HttpResponse(template.render(context))

def landing(request):
    return render(request, 'dayStarApp/landing.html')

# sitter views   
@login_required
def sitterReg(request):
    addSitterForm = Sitter_regForm(request.POST)
    message = None
    if request.method == 'POST':
        if addSitterForm.is_valid():
            newSitter = addSitterForm.save(commit = False)
            newSitter.save()
            message = "Sitter Added Successfully!"
        return redirect('home')
    return render(request, 'dayStarApp/sitter_reg.html', {'addSitterForm': addSitterForm, 'message': message})

def sitters(request): 
    all_sitters = Sitter.objects.all()
    context = {
        'all_sitters': all_sitters
    }
    template = loader.get_template('dayStarApp/sitters.html')
    return HttpResponse(template.render(context))

@login_required
def viewSitter(request, id): # sttier viewing page
    all_sitter = Sitter.objects.get(id=id)
    context = {
       'all_sitter': all_sitter
    }
    template = loader.get_template('dayStarApp/view_sitter.html')
    return HttpResponse(template.render(context))

def edit_page(request, item_id):
    item = Sitter.objects.get(pk=item_id)
    if request.method == 'POST':
        form = Sitter_regForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = Sitter_regForm(instance=item)
    return render(request, 'dayStarApp/edit_sitter.html', {'form': form})

# Baby views
@login_required
def babyRegistration(request):
    addBabyForm = Baby_regForm()
    message = None
    if request.method == 'POST':
        addBabyForm = Baby_regForm(request.POST)
        if addBabyForm.is_valid():
            newSitter = addBabyForm.save()
            message = "Baby Registered Successfully!"
            # Redirect to the 'babies' page after successful registration
            return redirect('babys')
    else:
        addBabyForm = Baby_regForm()

    return render(request, 'dayStarApp/baby_reg.html', {'addBabyForm': addBabyForm, 'message': message})

@login_required
def babys(request):
    all_babys = Baby.objects.all()
    context = {
        'all_babys': all_babys,
    }
    template = loader.get_template('dayStarApp/babies.html')
    return HttpResponse(template.render(context))

# supply views
@login_required
def supply(request):
    addSalesForm = Sales_regForm(request.POST)

    message = ""
    if request.method == 'POST':
        if addSalesForm.is_valid():
            message = "Sold item Added Successfully!"
            newSalesItem = addSalesForm.save(commit = False)
            newSalesItem.save()
        else:
            message = "Add a correct Item"
    return render(request, 'dayStarApp/supply.html', {'addSalesForm': addSalesForm, 'message': message, })

def deleteSitter(request, id):
    Sitter.objects.filter(id=id).delete()
    return redirect('/home')


def logout_view(request):
    logout(request)
    return redirect('/') # redirect user to the index page