class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
    
    def hello(self):
        print(f"Hello. This is {self.name}")
        
    def update_age(self, age):
        if age < 0:
            raise ValueError()
        else:
            self.age = age
            print(f"Now, I'm {self.age} years old.")
        
if __name__ == "__main__":
    man = Person("Jhon", 30)
    man.hello()    
    
    jhone = Person("Jhone", 30)
    jhone.update_age(31)
    
    