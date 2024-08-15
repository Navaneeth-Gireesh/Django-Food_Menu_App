from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_description', 'item_price', 'item_image']
        labels = {
            'item_name' : 'Name of the food',
            'item_description' : 'Describe the item',
            'item_price' : 'Price',
            'item_image': 'Upload Image Url'
        }
