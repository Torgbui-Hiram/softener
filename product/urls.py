from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product_view, name='product-view'),
    path('product/<product_id>', views.select_product, name='select-product'),
    path('select_item/<select_id>', views.item_select, name='select-item'),
    path('add_item/', views.add_item, name='add-item'),
    path('list_traders/', views.list_traders, name='list-traders'),
    path('add_traders/', views.add_traders, name='add-traders'),
    path('new_product/', views.add_product, name='new_pro'),
    path('edit_trader/<trader_id>', views.edit_trader_profile, name='edit_trader'),
    path('rm_p/<pro_id>', views.remove_product, name='remove'),
]
