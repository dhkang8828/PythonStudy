class A:
    def method(self):
        print("I'm A")
        
class B(A):
    def method(self):
        print("I'm B")
        
class C(A):
    def method(self):
        print("I'm C")
        
class D(B, C):
    pass

d = D()
d.method()

## 의사결정 Tree
print(D.mro())