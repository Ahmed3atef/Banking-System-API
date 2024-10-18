import uuid
from django.db import models
from accounts.models import CustomUser

class BankAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.email} - {self.account_number}"


class Transaction(models.Model):
    account_number = models.UUIDField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    TRANSACTION_TYPE = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"