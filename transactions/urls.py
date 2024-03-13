from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('create/', views.create_transaction, name='create_transaction'),
    path('<int:transaction_id>/delete/', views.delete_transaction, name='delete_transaction'),
]
