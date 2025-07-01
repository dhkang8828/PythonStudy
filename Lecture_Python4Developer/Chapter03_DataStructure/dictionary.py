'''
    Dictionary
    empty_dict = {}
    my_dict = {'key':1, 'key2':2, 'key3':3}
    
    dictionary[key]
    -. 복잡한 데이터를 구조화하여 관리 할 수 있다
'''
student1 = {
    '학번':'20230001',
    '이름':'홍길동',
    '전공':'컴퓨터공학',
    '학점':3.5,
    '성적': {'OS': 'A+', 'ComputerArchitecture': 'A+', 'Network': 'B+'}
}

student2 = {
    '학번':'20230002',
    '이름':'이순신',
    '전공':'정보통신공학',
    '학점':3.8,
    '성적': {'OS': 'C', 'ComputerArchitecture': 'A+', 'Network': 'B+'}
}

## 복합 딕셔너리
students = [student1, student2]
students[0]['성적']['OS'] = 'A'

''''
    keys(): 저장된 Key 목록 
    values(): 저장된 Value 목록
    items(): 저장된 Key-Value 쌍 목록
    get(key): key에 해당하는 value를 반환, 없으면 None 반환
    pop(key): key에 해당하는 value를 삭제하고 반환, 없으면 KeyError 발생
''' 
my_dict = {}
my_dict["key"] = "value"
print(f"my_dict: {my_dict}")  # {'key': 'value'}

person = {"name":"Alice", "age": 30, "city": "New York"}
name = person["name"]
print(f"name: {person['name']}, age:{person['age']}, home-town:{person['city']}.")  # Alice

##country = person["country"]     # KeyError 발생, 'country' 키가 존재하지 않음
##print(f"country: {country}")
country = person.get("country", "Unknown")  # 'country' 키가 없으면 'Unknown' 반환
print(f"country: {country}")  # Unknown

## dictionary value update
person["age"] = 35
person["country"] = "Korea" # 새로운 키 추가
print(f"country: {person["country"]}")  # Unknown

## 여러개의 dictionary를 합치기
person_details = {"country": "USA", "occupation": "Engineer", "hobby": "Reading"}
person.update(person_details)
print(f"Updated person: {person}")
print(f"Keys: {person.keys()}")  # dict_keys(['name', 'age', 'city', 'country', 'occupation', 'hobby'])

## Key 삭제
del person["hobby"]
print(f"After deleting hobby: {person}")  # {'name': 'Alice', '
