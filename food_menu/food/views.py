from django.shortcuts import render, get_object_or_404, redirect
from . models import Item
from . forms import AddItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.



class IndexClassView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'food_items'


class DetailsClassView(DetailView):
    model = Item
    template_name = 'details.html'


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

@login_required
def profile_request(request):
    return render(request, 'profile.html')