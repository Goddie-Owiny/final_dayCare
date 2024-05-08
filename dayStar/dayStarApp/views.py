from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from datetime import datetime


# Create your views here.
def landing(request):
    return render(request, 'dayStarApp/landing.html')


@login_required
def index(request):
    today_sitters = Sitter.objects.all().order_by('-id')
    today_babys = Baby.objects.all().order_by('-id')
    all_sitters = Sitter.objects.all()
    all_babys = Baby.objects.all()
    count_sitters = Sitter.objects.count()
    count_babys = Baby.objects.count()

    # all_sale = Sale.objects.all()
    context = {
        'today_babys': today_babys,
        'today_sitters': today_sitters,
        'count_sitters': count_sitters,
        'count_babys': count_babys,
        'all_sitters': all_sitters,
        'all_babys': all_babys,
        # 'all_sale': all_sale,
    }
    template = loader.get_template('dayStarApp/index.html')
    return HttpResponse(template.render(context))

# sitter views   
@login_required
def sitterReg(request):
    if request.method == 'POST':
        form = Sitter_regForm(request.POST)
        if form.is_valid():
            # If form is valid, create a Sitter object with validated cleaned data
            Sitter.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                location=form.cleaned_data['location'],
                contact=form.cleaned_data['contact'],
                education_Level=form.cleaned_data['education_Level'],
                religion=form.cleaned_data['religion'],
                next_of_kin=form.cleaned_data['next_of_kin'],
                recommended_by=form.cleaned_data['recommended_by'],
                sitter_number=form.cleaned_data['sitter_number'],
                NIN=form.cleaned_data['NIN']
            )
            message = "Sitter Added Successfully!"
            return redirect('sitters')  # Redirect to a sitters page
        else:
            message = "Sitter Registration Failed"
    else:
        form = Sitter_regForm()
        message = ""

    return render(request, 'dayStarApp/sitter_reg.html', {'form': form, 'message': message})
    
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
    if request.method == 'POST':
        form = Baby_regForm(request.POST)
        if form.is_valid():
            # If form is valid, create a baby object with validated cleaned data
            Baby.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                location=form.cleaned_data['location'],
                # period_of_stay=form.cleaned_data['period_of_stay'],
                baby_Number=form.cleaned_data['baby_Number'],
                brought_by=form.cleaned_data['brought_by'],
                parent_Name=form.cleaned_data['parent_Name'],
                status=form.cleaned_data['status']
            )
            message = "Sitter Added Successfully!"
            return redirect('babys')  # Redirect to a sitters page
        else:
            message = "Sitter Registration Failed"
    else:
        form = Baby_regForm()
        message = ""

    return render(request, 'dayStarApp/baby_reg.html', {'form': form, 'message': message})


@login_required
def babys(request):
    all_babys = Baby.objects.all()
    context = {
        'all_babys': all_babys,
    }
    template = loader.get_template('dayStarApp/babies.html')
    return HttpResponse(template.render(context))

def deleteBaby(request, id):
    Baby.objects.filter(id=id).delete()
    return redirect('/babies')



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