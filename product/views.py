from django.shortcuts import render, redirect
from .models import FabricSoftener, Traders
from .forms import SoftenerForm, TradersForm
from django.http import HttpResponseRedirect


def home(request):
    product = FabricSoftener.objects.all()
    return render(request, 'product/home.html', {'product': product})


# View products
def product_view(request):
    view = FabricSoftener.objects.all()
    return render(request, 'product/product.html', {'view': view})


def select_product(request, product_id):
    selected = FabricSoftener.objects.get(pk=product_id)
    return render(request, 'product/viewById.html', {'selected': selected})


# Select a single item from database
def item_select(request, select_id):
    selected = FabricSoftener.objects.get(pk=select_id)
    return render(request, 'product/select.html', {'selected': selected})


# Update a selected item to dtabase using form
def add_item(request):
    submitted = False
    if request.method == "POST":
        form = SoftenerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_item?submitted=True')
    else:
        form = SoftenerForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'product/add_item.html', {'form': form,
                                                     'submitted': submitted, })


# lIST AL TRADERS
def list_traders(request):
    trader_list = Traders.objects.all()
    return render(request, 'product/list_traders.html', {'trader_list': trader_list, })


# Add traders from site
def add_traders(request):
    submitted = False
    if request.method == "POST":
        form = TradersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_traders?submitted=True')
    else:
        form = TradersForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'product/add_traders.html', {'form': form,
                                                        'submitted': submitted, })


# add new product from site to database
def add_product(request):
    submitted = False
    if request.method == 'POST':
        form = SoftenerForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect('/new_product?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
        form = SoftenerForm()
        return render(request, 'product/new_product.html', {'form': form, 'submitted': submitted})


# edit and update trader profile
def edit_trader_profile(request, trader_id):
    model = Traders.objects.get(pk=trader_id)
    if request.method == 'POST':
        form = TradersForm(request.POST or None, instance=model)
        if form.is_valid:
            form.save()
            return redirect('list-traders')
    else:
        form = TradersForm(instance=model)
    return render(request, 'product/edit_trader.html', {'form': form, 'model': model})

