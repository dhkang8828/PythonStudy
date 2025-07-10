from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job
    
    def _hello(self):
        print(f"Hello. This is {self.name}, {self.__age} years old.")
        
    def update_age(self, age):
        if age < 0:
            raise ValueError()
        else:
            self.__age = age
            print(f"Now, I'm {self.age} years old.")
            
    @abstractmethod
    def introduce(self):
        pass
    
if __name__ == "__main__":
    print(f"Person")
    #man = Person("Jhon", 30)
    #man.hello()    
    
    #jhone = Person("Jhone", 30)
    #jhone.update_age(31)
    
    