from django.shortcuts import render, get_object_or_404, redirect
from . models import Item
from . forms import AddItemForm
# Create your views here.

def index(request):
    food_items = Item.objects.all()
    return render(request, 'index.html', {'food_items': food_items})

def details(request,item_id):
    food_details = get_object_or_404(Item, id=item_id)
    return render(request, 'details.html', {'food_details': food_details})

def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddItemForm()
    return render(request, 'add_item.html', {'form':form})

def edit_details(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = AddItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddItemForm(instance=item)
    return render(request, 'edit_details.html',{'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'delete_item.html',{'item': item})