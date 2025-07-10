from Chap06_01_ClassBasic import Person

class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job = "Actor")
        self.film = film
        
    def introduce(self):
        super()._hello()
        print(f"배우 이름: {self.name}, 대표작: {self.film}")
        
class Framer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, job = "Framer")
        self.fruit = fruit
        
    def introduce(self):
        super()._hello()
        print(f"농부 이름: {self.name}, 키우는 작물: {self.fruit}")
        