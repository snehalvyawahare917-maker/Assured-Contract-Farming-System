from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('farmer/', views.farmer, name='farmer'),
    path('farmer/register/', views.farmer_register, name='farmer_register'),
    path('farmer/login/', views.farmer_login, name='farmer_login'),
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('farmer/contracts/', views.farmer_contracts, name='farmer_contracts'),
    path('farmer/profile/', views.farmer_profile, name='farmer_profile'),
    path('farmer/crop/', views.farmer_crop, name='farmer_crop'),
    path('farmer/delivery/', views.farmer_delivery, name='farmer_delivery'),
    path('farmer/payment/', views.farmer_payment, name='farmer_payment'),

    path('admin-login/', views.admin_login, name='admin_login'),

    path('buyer/', views.buyer, name='buyer'),
    path('buyer/dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('buyer/register/', views.buyer_register, name='buyer_register'),
    path('buyer/login/', views.buyer_login, name='buyer_login'),
    path('buyer/logout/', views.buyer_logout, name='buyer_logout'),

    path('buyer/profile/', views.buyer_profile, name='buyer_profile'),
    path('buyer/contracts/', views.buyer_contracts, name='buyer_contracts'),
    path('buyer/available-farmers/', views.buyer_available_farmers, name='buyer_available_farmers'),
    path('farmer/edit-profile/', views.farmer_edit_profile, name='farmer_edit_profile'),
    path('buyer/edit-profile/', views.buyer_edit_profile, name='buyer_edit_profile'),
    path('contract/', views.contract, name='contract'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path(
    'admin-dashboard/update-delivery/<int:contract_id>/',
    views.update_delivery_status,
    name='update_delivery_status'
    ),

    path(
    'admin-dashboard/update-payment/<int:contract_id>/',
    views.update_payment_status,
    name='update_payment_status'
),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('farmer/logout/', views.farmer_logout, name='farmer_logout'),
]