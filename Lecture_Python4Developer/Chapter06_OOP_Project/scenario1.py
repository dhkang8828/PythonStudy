from account import SavingAccount, CheckingAccount
from user import BankUser

user1 = BankUser("Adam", money=1000)
## $200 - 입출금 계좌
user1.deduct_money(200)
account1 = CheckingAccount(holder_name=user1.get_name(), balance=200)
user1.add_account(account1)
## $800 - 예금 계좌
user1.deduct_money(800)
account2 = SavingAccount(holder_name=user1.get_name(), balance=800, interest_rate=0.05)
user1.add_account(account2)

## 예금 계좌 출금 가능
account2.unlock()

## 예금계좌에서 $400를 출금 후 사용자에게 지급
account2.withdraw(400)
user1.add_money(400)

## $400차감후 이를 입출금계좌로 입금
user1.deduct_money(400)
account1.deposite(400)

## 보유 현금 및 계좌목록 출력
user1.get_assets()

