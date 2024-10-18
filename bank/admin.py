from django.contrib import admin
from .models import BankAccount, Transaction

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'user', 'balance')
    search_fields = ('user__email', 'account_number')
    list_filter = ('user',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'amount', 'transaction_type', 'timestamp')
    search_fields = ('account__account_number', 'amount')
    list_filter = ('transaction_type', 'timestamp')