from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from . filters import *
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
    total_payments = Payment.objects.aggregate(total_amount=models.Sum('amount'))['total_amount'] or 0
    today_sitters = Sitter.objects.all().order_by('-id')
    today_babys = Baby.objects.all().order_by('-id')
    all_sitters = Sitter.objects.all()
    all_babys = Baby.objects.all()
    count_sitters = Sitter.objects.count()
    count_babys = Baby.objects.count()

    # all_sale = Sale.objects.all()
    context = {
        'total_payments': total_payments,
        'today_babys': today_babys,
        'today_sitters': today_sitters,
        'count_sitters': count_sitters,
        'count_babys': count_babys,
        'all_sitters': all_sitters,
        'all_babys': all_babys,
    }
    template = loader.get_template('dayStarApp/index.html')
    return HttpResponse(template.render(context))

# sitter views   
@login_required
def sitterReg(request):
    addSitterForm = Sitter_regForm(request.POST)  
    message = None
    if request.method == 'POST':
        if addSitterForm.is_valid():
            newSitter = addSitterForm.save(commit=False)  
            newSitter.save()
            message = "Sitter Added Successfully!"
            return redirect('sitters')
        else:
            message = "Sitter Registration Failed"
    else:
        addSitterForm = Sitter_regForm()  

    return render(request, 'dayStarApp/sitter_reg.html', {'addSitterForm': addSitterForm, 'message': message})

@login_required
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
def babyReg(request):
    addBabyForm = Baby_regForm(request.POST)  
    message = None
    if request.method == 'POST':
        if addBabyForm.is_valid():
            newBaby = addBabyForm.save(commit=False) 
            newBaby.save()
            message = "Baby Added Successfully!"
            return redirect('babys')
        else:
            message = "Baby Registration Failed"
    else:
        addBabyForm = Baby_regForm()  

    return render(request, 'dayStarApp/baby_reg.html', {'addBabyForm': addBabyForm, 'message': message})


@login_required
def babys(request):
    all_babys = Baby.objects.all().order_by('id')
    babysearch=BabyFilter(request.GET, queryset=all_babys)
    all_babys=babysearch.qs
    context = {
        'babysearch': babysearch,
        'all_babys': all_babys,
    }
    return render(request, 'dayStarApp/babies.html', {'all_babys': all_babys, 'babysearch': babysearch})

def deleteBaby(request, id):
    Baby.objects.filter(id=id).delete()
    return redirect('/babies')


# supply views
@login_required
def payment(request):
    if request.method == 'POST':
        form = Payment_regForm(request.POST)
        if form.is_valid():
            # If form is valid, create a baby object with validated cleaned data
            Payment.objects.create(
                baby=form.cleaned_data['baby'],
                period_of_stay=form.cleaned_data['period_of_stay'],
                amount=form.cleaned_data['amount'],
                # date_of_payment=form.cleaned_data['date_of_payment']    
            )
            message = "Payment made successfully"
            return redirect('index')  # Redirect to a index page
    else:
        form = Payment_regForm()
        message = ""

    return render(request, 'dayStarApp/payment.html', {'form': form, 'message': message})

@login_required
def sale(request):
    item_sell = Item_sellForm(request.POST)
    sell_message = None
    if request.method == 'POST':
        if item_sell.is_valid():
            newItem = item_sell.save(commit=False)
            newItem.save()
            sell_message = "Item Sold Successfully!"
            return redirect('sale')
        else:
            sell_message = "Item Sell failed!"
    else:
        item_sell = Item_sellForm()
    return render(request, 'dayStarApp/sale.html', {'item_sell': item_sell, 'sell_message': sell_message})

@login_required
def addItem(request):
    add_item_form = Item_regForm(request.POST)
    add_message = None
    if request.method == 'POST':
        if add_item_form.is_valid():
            newItem = add_item_form.save(commit=False)
            newItem.save()
            add_message = "Item Added Successfully!"
            return redirect('sale')
        else:
            add_message = "Item Addition failed!"
    else:
        add_item_form = Item_regForm()

    return render(request, 'dayStarApp/addStock.html', {'addItemForm': add_item_form, 'add_message': add_message})
  
@login_required
def deleteSitter(request, id):
    Sitter.objects.filter(id=id).delete()
    return redirect('/home')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/') # redirect user to the index page