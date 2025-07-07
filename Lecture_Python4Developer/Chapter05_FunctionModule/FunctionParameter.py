'''
    기본 매개변수
    
    def study(name, language="python")
    -. 기본 매개변수는 일반 매개변수 뒤에 위치
    
    키워드 인자
    -. 함수 호출 시 인자에 매개변수 이름을 넣어 전달
    def greet(name, greeting):
        print(f"name: {name} {greeting})
    greet(name="Alice", greeting="Hello")
    greet(greeting="Hi", name="Bob")
    
    가변 인자 리스트
    -. 
    def add_numbers(*args):     ##args는 실제로튜플의 형태로 정의됨, 
        result = 0
        for num in args:
            result += num
        return result
    add_number(1)
    add_number(1, 10, -15, 30)
    
    키워드 가변인자 리스트
    -. 가장 뒤에 위치해야 한다
    def print_key(**kwargs):
        for key, value in kwargs.items():
            print(f"key: {key}, value:{value})
    print_key(name="alpha", age=10)
    print_key(name="beta", country="USA")
    print_key(key="name")
    
    def display_info(name, *args, **kwargs):
        print(f"Name: {name})
        print(f"Known Language: {args}")
        for key, value in kwargs.items()
            print(f"key: {key}: {value}")
'''

##TAKA1
def func():
    var = "variable"    ## 지역변수 
    print (var)
#print(var)      ## Execution Error

var = "variable"        ## 전역 변수 
def func():
    print(var)

## 기본 매개변수 - 일반매개변수 뒤에 와야 한다.
def welcome(city, name="Guest"):
    print(f"Hello, {name}! this is {city}")
welcome("New York")
welcome("Kang", "Seattle")

def welcome2(city, name="Guest", room=None):
    if room == None:
        room = []
    room.append(101)
    print(f"Hello, {name}! this is {city}. You can use {room}")
welcome2("Seoul")
welcome2("Inchon", "Lee")

## 키워드 인자 
## 순서대로가 아닌 매개변수 이름에 인자 할당
def display_info(age, city, name="Guest"):
    print(f"Name: {name}, Age: {age}, City: {city}")
##display_info("Alice", 30, "New York") 
display_info(city="Seoul", name="Bob", age=22)

## 가변 인자 리스트 실습   
def cal_sum(*args):     ##기본적으로 tuble로 저장된다
    total = 0
    for arg in args:
        total += arg
    return total
print(f"cal_sum: {cal_sum(1,2,3,4,5)}")
print(f"cal_sum: {cal_sum(100, 500)}")

## 키워드 가변인자 리스트 
def print_info(**kwargs):
    for (key, value) in kwargs.items():
        print(f"P{key}:{value}")
print_info(name="Eve", age=20, city="Berlin")
info = {"name":"Charlie", "age":40, "City":"Tokyo"}
print_info(**info)

## list 전달은 어떻게 하는거지?
my_list = [1, 2, 3, 4, 5]
def print_list(list):
    for i, value in enumerate (list):
        print(f"idx:{i} = {value}")
print_list(my_list)
        


