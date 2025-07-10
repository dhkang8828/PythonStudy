from abc import ABC, abstractmethod
import random

class BankAccount(ABC):
    def __init__(self, holder_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        self._holder_name = holder_name
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
       
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
        
    
            