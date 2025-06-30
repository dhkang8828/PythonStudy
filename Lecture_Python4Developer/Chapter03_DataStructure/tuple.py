'''
    Tuple
    -. Tuple은 불변 속성
    가변 데이터: 정의된 이후에도 변경이 자유롭다 (list)
    불변 데이터: 변수의 값을 변경할 수 없다 (tuple)
    -. ()를 사용하고 각 항목은 쉼표로 구분
    empty_tuple = ()
    -. indexing, slicing, 연산도 list와 동일 
    
    Packing & Unpacking
    -. Packing: 여러 값을 하나의 변수에 할당하는 것
    tp = 1, 2, 3
    -. Unpacking: 하나의 변수에 할당된 값을 여러 변수로 나누는
    tp = (1, 2, 3)
    x, y, z = tp
    -. Unpacking시, 불필요한 값들은 _로 생략 가능
    x, _, _, y, z = (1, 2, 3, 4, 5)
'''
# empty Tuple
my_tuple = ()
## my_tuple.append(1) # AttributeError: 'tuple' object has no attribute 'append'
fruits = ("apple", "banana", "cherry", "blueberry", "kiwi")
fruit = fruits[2]  # "cherry"
print(f"third fruit: {fruit}")  # third fruit: cherry

## Packing & Unpacking
tp = 1, 2, 3, 4, 5
print(f"tp: {tp}")  
v1, v2, v3, v4, v5 = tp #Unpacking
print(f"v1: {v1}, v2: {v2}, v3: {v3}, v4: {v4}, v5: {v5}")  

## Swap code by Tuple
a = 10
b = 20
temp = a
a = b
b = temp

a, b = b, a ## packing & unpacking

## packing & unpacking 
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
val1, val2, val3, *vals = tp
print(f"val1: {val1}, val2: {val2}, val3: {val3}, vals: {vals}")  
val1, val2, val3, *vals, _ = tp
print(f"val1: {val1}, val2: {val2}, val3: {val3}, vals: {vals}")  
val1, val2, *vals, val9, _ = tp
print(f"val1: {val1}, val2: {val2}, vals: {vals}, val9: {val9}")  