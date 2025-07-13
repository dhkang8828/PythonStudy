from abc import ABC, abstractmethod
import random

class BankAccount(ABC):
    def __init__(self, holder_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        self._holder_name = holder_name
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def get_hoder_name(self):
        return self._holder_name
    
    def get_acount_number(self):
        return self._account_number
       
    def deposite(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError
        else:
            self.__balance -= amount
            return self.__balance
            
    @abstractmethod
    def info(self):
        pass

class SavingAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.__is_locked = True
        self.__interest_rate = interest_rate
        
    def withdraw(self, amount):
        if self.__is_locked == True:
            raise AttributeError
        else:
            return super().withdraw(amount)
        
    def unlock(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposite(interest)
        self.__is_locked = False
        
    def info(self):
        print(f"[예금/{self.get_acount_number()}]" +
              f" 잔액 ${self.get_balance()}," +
              f" 이율:{self.__interest_rate * 100}, 출금 제한:{self.__is_locked}")

class CheckingAccount(BankAccount):
    def __init__(self, holder_name, balance, withdraw_limit = 500):
        super().__init__(holder_name, balance)
        self.__withdraw_limit = withdraw_limit
        
    def update_limit(self, new_limit):
        self.__withdraw_limit = new_limit
        
    def withdraw(self, amount):
        if (self.__withdraw_limit < amount):
            raise ValueError
        else:
            return super().withdraw(amount)
        
    def info(self):
        print(f"[입출금/{self.get_acount_number()}]" + 
              f" 잔액 ${self.get_balance()}," + 
              f" 출금한도 ${self.__withdraw_limit}")