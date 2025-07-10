from Chap06_02_MajorConcept import Programmer
from Chap06_04_Inheritance import Actor, Framer

## 추상화
dave = Programmer(name="Dave", age=52, language="Python")
dave.introduce()

song = Actor(name="Song", age=38, film="Kingdom of Heaven")
song. introduce()

Han = Framer(name="Han", age=44, fruit="Mango")
Han.introduce()

## 다형성
People = [ 
    Programmer(name="Dave", age=52, language="Python"), 
    Actor(name="Song", age=38, film="Kingdom of Heaven"),
    Framer(name="Han", age=44, fruit="Mango")
]

for person in People:
    person.introduce()
    
## Encapsulation
robert = Programmer(name="robert", age=22, language="CPP")
## robert.age = -1     
robert._hello()