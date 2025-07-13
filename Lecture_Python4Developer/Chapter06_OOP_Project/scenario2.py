from account import BankAccount, CheckingAccount, SavingAccount
from user import BankUser

user2 = BankUser(name="Brian", money=900)

## 입출금 계좌에 $800
user2.deduct_money(800)
account1 = CheckingAccount(holder_name=user2.get_name(), 
                           balance=800)
user2.add_account(account1)

## 6% 예금 계좌에 $100
user2.deduct_money(100)
account2 = SavingAccount(holder_name=user2.get_name(), 
                         balance=100, interest_rate=0.06)
user2.add_account(account2)

## 입출금 계좌에서 $800 출금 시도
try:
    account1.withdraw(800)
except ValueError:
    account1.update_limit(800)
    account1.withdraw(800)
finally:
    user2.add_money(800)
    
user2.get_assets()