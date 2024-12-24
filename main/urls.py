from django.urls import path
from . import views
from .views import bouquets_view

urlpatterns = [
    path('', views.bouquets_view, name='home'),
    path('about', views.about, name='about'),
    path('delivery', views.delivery, name='delivery'),
    path('bouquets/ ', bouquets_view, name='bouquets'),
    path('order', views.order, name='order'),
    path('add-to-order/<int:bouquet_id>/', views.add_to_order, name='add_to_order'),
    path('remove-from-order/<int:bouquet_id>/', views.remove_from_order, name='remove_from_order'),
    path('update-order-quantity/<int:bouquet_id>/', views.update_order_quantity, name='update_order_quantity'),
    path('order-success', views.orderSuccess, name='order-success')
]