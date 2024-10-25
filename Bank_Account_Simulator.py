'''2. Bank Account Simulator
Problem Statement: Design a bank account simulator to manage savings, withdrawals, and transfers between accounts.
Steps:
Create an Account class with attributes like balance and account number.
Add methods for depositing, withdrawing, and transferring funds.
Implement error handling for overdrafts and invalid transactions.'''

class Account():
    def __init__(self, account_no, balance = 0.0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        '''To add funds to an account'''
        if amount <= 0:
            print('Deposited amount must be positive')
            return False
        self.balance += amount
        print(f"Deposited Rs. {self.balance} to your account {self.account_no}.")
        return True
    
    def withdrawl(self, amount):
        '''To withdraw funds from the account balance if have sufficient balance'''

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print("Insufficient Balance")
        self.balance -= amount
        print(f"withdrawl Rs. {amount} from the account Rs. {self.account_no}. New balance is {self.balance}.")
        return True
    
    def Transfer(self, target_account, amount):
        '''To Transfer funds to another account if sufficient balance.'''
        if self.withdrawl(amount):
            target_account.deposit(amount)
            print(f"Transferred Rs. {amount} from account {self.account_no}. ")
            return True
        print("Transfer failed dur to insufficient funds in account.}")
        return False
    
    def get_balance(self):
        '''To retrun the current balance of the account.'''
        return self.balance
    
if __name__  == '__main__':
    
    account1 = Account('1234', 1000)
    account2 = Account('2345', 500)

    account1.deposit(200)
    account2.withdrawl(300)

    account1.Transfer(account2, 300)

print(f'final balance in account {account1.account_no}: Rs. {account1.get_balance}')
print(f'final balance in account {account2.account_no}: Rs. {account2.get_balance}')

