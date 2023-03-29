from django.db import models

# Create your models here.
class Accounts(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    date_opened = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    balance = models.DecimalField(max_digits = 20, decimal_places = 2)
    
    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        
    def __str__(self):
        return str("Account #" + str(self.id) + ": " + self.first_name + " " + self.last_name + "  -----Current Balance-----: $" + str(self.balance))
        
    

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
    starting_balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    ending_balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    
    
    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        
    def save(self, *args, **kwargs):
        """
        Save method sets the Transaction.starting_balance = Account.account_id.balance
        Then attempts to calculate the Transaction.ending_balance based on self.transaction_type
        Error handles negative number, 0, or transaction_amt greater than balance (in case of withdrawal)
        """
        #starting_balance set to current balance of Account.id
        self.starting_balance = self.account_id.balance
        
        #DEPOSIT
        #calculate ending_balance based on transaction_amt and starting_balance
        if self.transaction_type == 'DP':
            if self.transaction_amt <= 0:
                raise ValueError("Transaction amount must be greater than 0.")
            try:
                self.ending_balance = self.starting_balance + self.transaction_amt
                
            except ValueError:
                raise ValueError('Invalid transaction amount.')
                
        #WITHDRAWAL
        elif self.transaction_type == 'WD':
            #checks if starting_balance >= transaction_amt for withdrawal
            if self.transaction_amt <=0:
                raise ValueError("Transaction amount must be greater than 0.")
            if self.starting_balance <= self.transaction_amt:
                raise ValueError("Transaction amount must be less than starting balance.")
            try: 
                self.ending_balance = self.starting_balance - self.transaction_amt
                
            except ValueError:
                raise ValueError('Invalid transaction amount.')
         
        #TRANSFER
        #TODO: FUTURE BUILD TRANSFER CAPABILITY BETWEEN ACCOUNTS
        
        
        #updating balance of the account
        self.account_id.balance = self.ending_balance
        self.account_id.save()
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return str(str(self.account_id) + "----------- Transaction #" + str(self.id) + ": Timestamp: " + str(self.timestamp) + " Type: " + self.transaction_type)