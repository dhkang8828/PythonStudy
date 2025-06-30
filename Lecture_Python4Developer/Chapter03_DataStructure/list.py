'''
    List
    -. Sequence Type 
    -. 각 요소들이 다른 데이터 타입으로 구성 되어도 괜찮다.
    -. 순서대로 값을 저장 
    -. 배열과 유사
'''
my_list = [10, 20, 30, 40, 50]
print(f"my_list: {my_list}")

my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)
my_list.append(70)
print(f"my_list: {my_list}")

print(f"len(my_list): {len(my_list)}")

## indexing
element = my_list[3]
print(f"element: {element}")  # IndexError: list index out of range 

## Slicing
sliced = my_list[3:]
print(f"sliced: {sliced}")  # [40, 50, 60, 70]

## is included?
fruits = ['apple', 'banana', 'cherry', 'blueberry', 'kiwi']
print(f"fruits: {fruits}")  # ['apple', 'banana', 'cherry', 'blueberry', 'kiwi']
is_banana_included = "banana" in fruits  # True
print(f"is_banana_included: {is_banana_included}")  # True

## index
index_of_cherry = fruits.index("cherry")  # 2
print(f"index_of_cherry: {index_of_cherry}")  # 2
index_of_mango = fruits.index("mango") if "mango" in fruits else -1  # -1
print(f"index_of_mango: {index_of_mango}")  # -1

## Sort
numbers = [4, 2, 1, 3, 8, 6, 7, 5, 9, 10]
print(f"unsorted numbers: {numbers}")  # [4, 2, 1, 3, 8, 6, 7, 5, 9, 10]
numbers.sort()
print(f"sorted numbers: {numbers}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.sort(reverse=True)
print(f"reverse sorted numbers: {numbers}") 

## list
my_list = []
my_list.append(10)
my_list.append(11)
my_list.append(12)
print(f"my_list: {my_list}")  
## Extend
my_list.extend([13, 14, 15])
print(f"my_list after extend: {my_list}")  
## 복합리스트
my_list.append([16, 17, 18])     
print(f"my_list after append: {my_list}")  
print(f"my_list[-1]: {my_list[-1]}")  # [16, 17, 18]

## list operations
my_list = [10, 11, 12, 13, 14, 15]
my_list + [16, 17, 18]  
print(f"my_list + [16, 17, 18]: {my_list + [16, 17, 18]}")  

multi_list = [0, 1, 2, 3]
print(f"multi_list: {multi_list * 3}")

## delete elements
my_list = [10, 11, 12, 13, 14, 15]
del my_list[0]
my_list.pop(0)
print(f"my_list after del my_list[0]: {my_list}")  

max_value = max(my_list)
min_value = min(my_list)
print(f"max_value: {max_value}, min_value: {min_value}")