from django.urls import path
# from .views import expense_create_view, expense_list_api_view, expense_retrieve_api_view, expense_put_update_api_view, expense_delete_api_view
# from .views import ExpenseCreateAPIView,\
#     ExpenseListAPIView,\
#     ExpenseRetrieveAPIView,\
#     ExpenseUpdateAPIView,\
#     ExpenseDeleteAPIView
from .views import ExpenseListCreateAPIView, ExpenseRetrieveUpdateDeleteView


urlpatterns = [
    path('<int:pk>/', ExpenseRetrieveUpdateDeleteView.as_view()),
    path('', ExpenseListCreateAPIView.as_view()),
]

















# urlpatterns = [
#     path('create/', ExpenseCreateAPIView.as_view()),
#     path('list/', ExpenseListAPIView.as_view()),
#     path('expense/<int:pk>/', ExpenseRetrieveAPIView.as_view()),
#     path('expense-update/<int:pk>/', ExpenseUpdateAPIView.as_view()),
#     path('expense-delete/<int:pk>/', ExpenseDeleteAPIView.as_view()),
# ]










# urlpatterns = [
#     path('create/', expense_create_view, name='expense_create'),
#     path('list/', expense_list_api_view, name='expenses_list'),
#     path('expense/<int:pk>/', expense_retrieve_api_view, name='expense_detail' ),
#     path('expense-update/<int:pk>/', expense_put_update_api_view, name='expense_detail' ),
#     path('expense-delete/<int:pk>/', expense_delete_api_view, name='expense_delete')
# ]
