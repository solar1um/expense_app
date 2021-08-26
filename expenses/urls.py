from django.urls import path
from .views import expense_create_view, expense_list_api_view, expense_retrieve_api_view

urlpatterns = [
    path('create/', expense_create_view, name='expense_create'),
    path('list/', expense_list_api_view, name='expenses_list'),
    path('expense/<int:pk>/', expense_retrieve_api_view, name='expense_detail' )
]
