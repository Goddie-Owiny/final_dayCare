from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseBadRequest
from .forms import *
from . filters import *
from .models import *
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
from django.contrib.auth import logout

from django.contrib import messages


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
    all_onduty = Sitter_on_duty.objects.count()
    item_sell = ItemSelling.objects.aggregate(total=Sum('amount_paid'))
    baby_payments = BabyPayment.objects.aggregate(total=Sum('amount_paid'))
    # total_payments = item_sell['total'] + baby_payments['total']

    context = {
        # 'total_payments': total_payments,
        'today_babys': today_babys,
        'today_sitters': today_sitters,
        'count_sitters': count_sitters,
        'count_babys': count_babys,
        'all_sitters': all_sitters,
        'all_babys': all_babys,
        'all_onduty': all_onduty,
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

@login_required
def edit_sitterdetails(request, id):
    item = get_object_or_404(Sitter, id=id)
    if request.method == 'POST':
        form = Sitter_regForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('sitters')  # Redirect to a success page
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
    return render(request, 'dayStarApp/babies.html', {'all_babys': all_babys, 'babysearch': babysearch})

@login_required
def viewBaby(request, baby_id): # sttier viewing page
    all_baby = Baby.objects.get(id=baby_id)
    context = {
       'all_baby': all_baby
    }
    template = loader.get_template('dayStarApp/view_baby.html')
    return HttpResponse(template.render(context))

@login_required
def edit_babydetails(request, baby_id):
    baby = get_object_or_404(Baby, id=baby_id)
    if request.method == 'POST':
        baby = Baby_regForm(request.POST, instance=baby)
        if baby.is_valid():
            baby.save()
            return redirect('babys')  # Redirect to a babies page
    else:
        baby = Baby_regForm(instance=baby)
    return render(request, 'dayStarApp/edit_baby.html', {'baby': baby})


@login_required
def deleteBaby(request, id):
    Baby.objects.filter(id=id).delete()
    return redirect('/babies')


#sell item form
@login_required
def sale(request):
    itemform = Item_sellForm(request.POST)
    sell_message = None
    if request.method == 'POST':
        if itemform.is_valid():
            newItem = itemform.save(commit=False)
            newItem.save()
            sell_message = "Item Sold Successfully!"
            return redirect('sale')
        else:
            sell_message = "Item Sell failed!"
    else:
        itemform = Item_sellForm()
    item = AddItem.objects.all()
    return render(request, 'dayStarApp/sale.html', {'itemform': itemform, 'item': item, 'sell_message': sell_message})

@login_required
def selling(request, pk):
    sell = AddItem.objects.get(id=pk)
    form = Item_sellForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            newItem = form.save(commit=False)
            newItem.doll_name = sell
            newItem.amount_paid = sell.price
            newItem.save()
            sell_quantity = int(request.POST['quantity'])
            sell.quantity -= sell_quantity
            sell.save()
            return redirect('sale')
    return render(request, 'dayStarApp/selling.html', {'form': form})

@login_required
def salesrecord(request):
    sales = ItemSelling.objects.all()
    total = sum([item.amount_paid for item in sales if item.amount_paid is not None])
    change = sum([item.get_change() for item in sales if item.get_change() is not None])
    net = total - change
    return render(request, 'dayStarApp/salerecord.html', {'total': total, 'sales': sales, 'total': total, 'net': net, 'change': change})

#adding stock to sale
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
def onduty(request):
    if request.method == 'POST':
        form = Sitter_dutyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allonduty')
    else:
        form = Sitter_dutyForm()
    return render(request, 'dayStarApp/onduty.html', {'form': form})

@login_required
def allonduty(request):
    duty = Sitter_on_duty.objects.all()
    context ={
        'duty': duty,
    }
    template = loader.get_template('dayStarApp/allOnduty.html')
    return HttpResponse(template.render(context))
    
@login_required
def editOnduty(request, id):
    edited = get_object_or_404(Sitter_on_duty, id=id)
    if request.method == 'POST':
        form = Sitter_dutyForm(request.POST, instance=edited)
        if form.is_valid():
            form.save()
            return redirect('allonduty')
    else: 
        form = Sitter_dutyForm(instance=edited)
    return render(request, 'dayStarApp/editOnduty.html', {'form': form, 'edited': edited})

@login_required
def addmore(request, id):
    issue_doll = AddItem.objects.get(id=id)
    if request.method == 'POST':
        form = Addmore(request.POST)
        if form.is_valid():
            moreStock = request.POST.get('quantity')
            if moreStock:
                try:
                    added = int(moreStock)
                    issue_doll.quantity += added
                    issue_doll.save()
                    print(added)
                    print(issue_doll.quantity)
                    return redirect('sale')
                except ValueError:
                    return HttpResponseBadRequest('Invalid quantity')
    else:
        form = Addmore()
    return render(request, 'dayStarApp/addmore.html', {'form': form })

#views for baby payments
@login_required
def babyPay(request):
    baby = BabyPayment.objects.all()
    return render(request, 'dayStarApp/babypay.html', {'baby': baby })

@login_required
def babyadd(request):
    if request.method == 'POST':
        form = BabyPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('babypay')
    else: 
        form = BabyPaymentForm()
    return render(request, 'dayStarApp/babyadd.html', {'form': form})

@login_required
def babyedit(request, id):
    edited = get_object_or_404(BabyPayment, id=id)
    if request.method == 'POST':
        form = BabyPaymentForm(request.POST, instance=edited)
        if form.is_valid():
            form.save()
            return redirect('babypay')
    else: 
        form = BabyPaymentForm(instance=edited)
    return render(request, 'dayStarApp/babyedit.html', {'form': form, 'edited': edited})
    

#sitter payment views
@login_required
def sitterpay(request):
    sitter = SitterPayment.objects.all()
    return render(request, 'dayStarApp/sitterpay.html', {'sitter': sitter })

@login_required
def sitteradd(request):
    if request.method == 'POST':
        form = SitterPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sitterpay')
    else: 
        form = SitterPaymentForm()
    return render(request, 'dayStarApp/sitteradd.html', {'form': form})

@login_required
def sitteredit(request, id):
    edited = get_object_or_404(SitterPayment, id=id)
    if request.method == 'POST':
        form = SitterPaymentForm(request.POST, instance=edited)
        if form.is_valid():
            form.save()
            return redirect('sitterpay')
    else: 
        form = SitterPaymentForm(instance=edited)
    return render(request, 'dayStarApp/sitteredit.html', {'form': form, 'edited': edited})

#other Stocked items
@login_required
def stock(request):
    stocks = Stock.objects.all()
    if request.method == 'POST':
        stockform = StockForm(request.POST)
        if stockform.is_valid():
            stockform.save()
            return redirect('stock')
    else: 
        stockform = StockForm()
    return render(request, 'dayStarApp/otherstock.html', {'stockform': stockform , 'stocks': stocks})

@login_required
def issuestock(request, pk):
    issue = Stock.objects.get(id=pk)
    issueform = IssueForm(request.POST)
    if request.method == 'POST':
        if issueform.is_valid():
            newStock = issueform.save(commit=False)
            newStock.stock_name = issue
            newStock.save()
            issue_quantity = int(request.POST['quantity'])
            issue.quantity -= issue_quantity
            print(issue.quantity)
            issue.save()
            return redirect('stock')
    return render(request, 'dayStarApp/issuestock.html', {'issueform': issueform})

@login_required
def addstock(request, pk):
    add_stock = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form = AddexistingStock(request.POST)
        if form.is_valid():
            moreStock = request.POST.get('quantity')
            if moreStock:
                try:
                    added = int(moreStock)
                    add_stock.quantity += added
                    add_stock.save()
                    print(added)
                    print(add_stock.quantity)
                    return redirect('stock')
                except ValueError:
                    return HttpResponseBadRequest('Invalid quantity')
    else:
        form = AddexistingStock()
    return render(request, 'dayStarApp/add.html', {'form': form })

@login_required
def editstock(request, id):
    editedstock = get_object_or_404(Stock, id=id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=editedstock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    else: 
        form = StockForm(instance=editedstock)
    return render(request, 'dayStarApp/editedstock.html', {'form': form, 'editedstock': editedstock})


@login_required
def issuedstock(request):
    issued = Issue_Stock.objects.all()
    return render(request, 'dayStarApp/issuedstock.html', {'issued': issued })

# authetications
@login_required
def deleteSitter(request, id):
    sitter = Sitter.objects.get(id=id)
    if request.method == 'POST':
        # If the confirmation form is submitted
        if 'confirm_delete' in request.POST:
            # Delete the sitter
            sitter.delete()
            return redirect('sitters')
        elif 'cancel_delete' in request.POST:
            return redirect('sitters')
    return render(request, 'dayStarApp/sitters.html', {'sitter': sitter})

@login_required
def logout_view(request):
    logout(request)
    return redirect('/') # redirect user to the index page