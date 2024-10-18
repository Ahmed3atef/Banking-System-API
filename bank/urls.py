from django.urls import path
from .views import BankAccountListCreateView, TransactionCreateView

urlpatterns = [
    path('accounts/', BankAccountListCreateView.as_view(), name='account-list-create'),
    path('transactions/', TransactionCreateView.as_view(), name='transaction-create'),
]