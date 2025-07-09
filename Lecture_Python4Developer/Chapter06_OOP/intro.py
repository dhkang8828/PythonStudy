'''
    Object Oriented Programming (OOP)
    
    -. 인간의 인지방식과 가장 유사
    -. 실제 세계를 모델링 하는데에 적합
    -. 유지보수의 용이성 
    
    Object
    -. Member Variable + Member Function 
    -. 현실 세계의 개념, 사물을 프로그램에서 모델링 한 것
    
    Class
    -. 객체의 초기 상태값과 기능에 대한 구현
    -. 객체를 만들기 위한 설계도
    class Person:
        def hello(self):    ##메소드 정의 시 첫 파라미터는 반드시 self
            print("Hello!")
    
    멤버 변수
    -. 객체가 가지는 속성(Attribute) 또는 값(Value, Data)
    -. 멤버 변수로의 접근: Obj.
    
    생성자
    -. __init()__ 이라는 이름으로 예약되어 있음
    -. 생성자의 첫 번째 매개변수는 항상 "self"
    
    class Person:
        def hello(self):
            print("Hello! I'm" + self.name)
            
        def __init__(self, name, age):
            self.name = name
            self.age = age
            
    man = Person("Robert", 30)
    man.hello()
    woman = Person("Julia", 33)
    
    ## 메소드(Method)
    -. 첫 번째 인자는 반드시 self 이여야 한다.
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def hello(self):
            print("Hello! I'm" + self.name)
            
        def update_age(self, new_age):
            if new_age > 0:
                self.age = new_age
                print(f"I'm {self.age} years old.")
            else:
                raise ValueError("age must over zero")
''' 
