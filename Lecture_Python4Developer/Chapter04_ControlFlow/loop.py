'''
    반복문
    특정 작업을 반복해서 수행
    
    1) for 
    numbers = [1, 2, 3, 4, 5]
    
    for number in numbers:
        print(number)
    else:
        print("Done Print")
        
    -. range([start], stop, [step])
    for i in range(5):
        print(i)    # 0 1 2 3 4
    for i in range(1, 5, 2):
        print(i)    # 1, 3
        
    -. enumerate()
    시퀀스 순회하며, 요소와 인덱스 쌍을 튜플로 반환
    fruits = ["apple", "banana", "cherry", "strawberry"]
    
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}번째 과일: {fruit})
        
    2) while
    특정 조건이 True인 동안 반복 
    
    counter = 0
    while counter < 3:
        print(f"cnt: {counter}")
        counter = counter + 1
    else:
        print("done while loop")
        
    3) break and continue
    -. break: 현재 수행 중인 반복문 중단
    -. continue: 현재 수행 중인 구문 jump
    
    4) pass = TODO랑 유사하다.
'''

## for loop
for i in range(5):
    print(f"i: {i}")
else:
    print("done for loop")
print("\n\n")

## while loop
cnt = 0
while cnt < 5:
    print(f"cnt: {cnt}")
    cnt = cnt + 1
else:
    print("done while")
print("\n\n")
    
fruits = ["apple", "strawberry", "peach", "korean-melon", "banana"]
for fruit in fruits:
    if fruit == "apple":
        print(f"Apple is red")
    print(f"{fruit} is in bucket")
print("\n\n")    

'''
## 무한 loop
while (True):
    user_input = input("please input command: ")
    if user_input == "exit":
        break
    else:
        pass        ## TODO: implement later
'''

## 구구단 프로그램
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} x {y} = {x * y}")
    print("\n")
    
## Enumerate
for idx, fruit in enumerate(fruits):
    print(f"idx[{idx}]: {fruit}")
print("\n")

## Factorial
result = 1
factorial = int(input("input factorial value: "))
for i in range(1, factorial):
    result = result * i
print(f"{factorial}! = {result}")

        

    