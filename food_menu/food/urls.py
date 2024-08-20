from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('details/<int:item_id>', views.details, name = 'details'),
    path('add_item', views.add_item, name = 'add_item'),
    path('edit_details/<int:item_id>', views.edit_details, name = 'edit_details'),
    path('delete_item,<int:item_id>', views.delete_item, name = 'delete_item'),
    path('profile/', views.profile_request, name = 'profile')
]
