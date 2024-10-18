from rest_framework import serializers
from .models import BankAccount, Transaction

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['account_number', 'balance']


class TransactionSerializer(serializers.ModelSerializer):
    # Accept account_number instead of account
    account_number = serializers.UUIDField(write_only=True)
    account_balance = serializers.DecimalField(source='bankaccount.balance', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Transaction
        fields = ['account_number', 'amount', 'transaction_type', 'timestamp', 'account_balance']

    def create(self, validated_data):
        # Extract account_number from validated_data
        account_number = validated_data.pop('account_number')

        # Fetch the related bank account using the account_number
        try:
            account = BankAccount.objects.get(account_number=account_number)
        except BankAccount.DoesNotExist:
            raise serializers.ValidationError("Account with this account number does not exist.")

        # Create the transaction and associate it with the fetched account_number
        transaction = Transaction.objects.create(account_number=account_number, **validated_data)

        # Update the balance based on transaction type
        if transaction.transaction_type == 'deposit':
            account.balance += transaction.amount
        elif transaction.transaction_type == 'withdrawal':
            if account.balance >= transaction.amount:
                account.balance -= transaction.amount
            else:
                raise serializers.ValidationError({"detail": "Insufficient balance for withdrawal"})

        # Save the updated account balance
        account.save()

        return transaction