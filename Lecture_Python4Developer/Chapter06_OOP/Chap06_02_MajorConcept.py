'''
    1. 상속
    -. 부모클래스를 활용하여 새로운 클래스를 정의
    -. 부모 클래스: 보다 포괄적이고, 공통의 개념과 메소드 정의
    -. 자식 클래스: 조금 더 구체적인 개념과 메소드
    -. class Children(Parent): ...
    
    -. 자식은 super() 예약어를 활용하여 부모 메소드 접근 가능
    -. Method Overriding도 가능
    
    -. 다중 상속 가능
        -. 둘 이상의 부모 클래스 상속 가능 
        class Children(Parent1, Parent2): ... 
        -. 문제점: 다이아몬드 상속! 
        class A
        class B(A), class C(A)
        class D(B, C)
            d = D()
            d.method() ## 어떤 메소드가 호출? 
    
    2. 추상화
    -. 복잡한 구조를 모델링을 통해 필수 동작들로 단순화 하는 과정
        > 다양한 객체의 공통점을 찾고, 이를 포괄하는 상위 추상 클래스 정의
        > Rectangle, Triangle -> Shame class, getArea(), getDraw() ... 
    -. 추상 클래스를 위한 표준 라이브러리: abc
    from abc import ABC, abstractmethod
    
    class Shape(ABC): 
    
    3. 캡슐화
    -. 객체의 데이터와 관련 메소드를 묶어 외부로부터 보호하는 개념
    -. 객체의 속성은 기본적으로 외부에서 접근 불가
        > 객체 외부에서 접근 가능한 기능: Public
        > 객체 내부에서만 접근 가능한 기능: Private (__)
        > 상속 받은 객체에서 접근 가능: Protected (_)
        
    4. 다형성
    -. 다양한 클래스들이 동일한 이름의 메소드를, 각자의 목적에 맞게 사용
'''
from Chap06_01_ClassBasic import Person

class Programmer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age, job="Programmer") ##생성자 호출
        self.language = language
    
    def introduce(self):
        super()._hello()
        print(f"I'm Programmer, I can use {self.language}")

