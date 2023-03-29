from django.db import models

# Create your models here.
class Accounts(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    date_opened = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    current_amt = models.DecimalField(max_digits = 20, decimal_places = 2)
    
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        
    def __str__(self):
        return str("Account #" + str(self.id) + ": " + self.first_name + " " + self.last_name)
        
    

class Transactions(models.Model):
    ACCOUNT_OPENED = 'AO'
    ACCOUNT_CLOSED = 'AC'
    WITHDRAWAL = 'WD'
    DEPOSIT = 'DP'
    TRANSFER = 'TR'
    
    TRANSACTION_TYPES = [
        (ACCOUNT_OPENED, 'Account Opened'),
        (ACCOUNT_CLOSED, 'Account Closed'),
        (WITHDRAWAL, 'Withdrawal'),
        (DEPOSIT, 'Deposit'),
        (TRANSFER, 'Transfer'),
    ]
    
    timestamp = models.DateTimeField()
    account_id = models.ForeignKey(Accounts, on_delete=models.PROTECT, related_name = "account_id")
    transaction_amt = models.DecimalField(max_digits = 20, decimal_places = 2)
    transaction_type = models.CharField(max_length=2, choices = TRANSACTION_TYPES)
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
    
    def __str__(self):
        return str(str(self.account_id) + "----------- Transaction # :" + str(self.id) + ": Timestamp: " + str(self.timestamp) + " Type: " + self.transaction_type)