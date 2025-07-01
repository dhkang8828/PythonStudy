'''
    Set
    -. 집합 자료형
    -. 중복을 허용하지 않음
    -. 순서가 없음
    -. {} or set()
    my_set = {1, 2, 2, 3}  # {1, 2, 3}
      good_set = set("Good") # {'G', 'o', 'd'}
      empty_set = set()
    -. 
      add()
      update()
      remove()
    -. 연산
      합집합: union() or |
      교집합: intersection() or &
      차집합: difference() or -
      대칭차집합: symmetric_difference() or ^
'''
empty_set = set()
my_set = {1, 2, 3, 3, 4}
print(f"my_set: {my_set}")  # {1, 2, 3, 4}

empty_set = {}  ## this is a dictionary, not a set
empty_set = set()  # correct way to create an empty set

fruits = {"apple", "banana", "cherry", "blueberry", "kiwi"}
print(f"fruits: {fruits}")  

## Add
fruits.add("orange")
print(f"fruits after add: {fruits}")  
## delete
fruits.remove("banana")  
print(f"fruits after remove: {fruits}") 
fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}

## Union(합집합)
union_fruits = fruits1.union(fruits2)
union_fruits = fruits1 | fruits2
print(f"Union of fruits1 and fruits2: {union_fruits}")  # {'apple', 'strawberry', 'peach', 'banana', 'orange'}

## Intersection(교집합)
intersection_fruits = fruits1.intersection(fruits2)
intersection_fruits = fruits1 & fruits2
print(f"Intersection of fruits1 and fruits2: {intersection_fruits}")  

## Difference(차집합)
difference_fruits_1 = fruits1.difference(fruits2)
difference_fruits_1 = fruits1 - fruits2
print(f"Difference of fruits1 and fruits2: {difference_fruits_1}")
difference_fruits_2 = fruits2.difference(fruits1)
difference_fruits_2 = fruits2 - fruits1
print(f"Difference of fruits2 and fruits1: {difference_fruits_2}")