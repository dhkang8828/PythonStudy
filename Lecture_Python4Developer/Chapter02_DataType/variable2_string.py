'''
    문자열
    
    1. 문자열 사칙 연산
    문자열 더하기
    str1 + str2
    문자열 곱하기
    str * n
    
    2. 문자열 
    문자열 길이: len(str)
    
    3. 인덱싱
    str[3]
    str[-1]
    
    4. 슬라이싱
    str[0:3] # 0부터 2까지
    str[:3]  # 처음부터 2까지
    str[3:]  # 3부터 끝까지
    str[-3:] # 뒤에서 3개
    str[-3:-1] # 뒤에서 3번째부터 -1번째까지 (
        
    5. 문자열 속성
    count(str, sub) # sub가 str에 몇번 나오는지
    find(str, sub)  # sub가 str에 처음 나오는 위치
    index(str, sub) # sub가 str에 처음 나오는 위치 (없으면 에러)
    replace(str, old, new) # str에서 old를 new로 바꿈
    split(str, sep) # str을 sep로 나눔
    join(list) # list의 문자열을 합침
    upper(str) # 대문자로 변환
    lower(str) # 소문자로 변환
    strip(str) # 양쪽 공백 제거
    isalpha(str) # 알파벳인지 확인
    isdecimal(str) # 숫자인지 확인
    ... 등등
    
    6. 문자열 활용하기: 문자열 만들기
    문자열 안에 변수 또는 값 삽입
    1) %연산자 사용
      %s, %d, %f 등으로 표현
        "Today's temperature is %d degrees. (day:%d)" % (25, 20)    
    2) format() 메서드 사용
        "Today's temperature is {0} degrees. (day:{1})".format(25, 20)
    3) 포멧 스트링 사용하기 (3.6 이상)
        f"Today's temperature is {weather} degrees. (day:{temp+1})"
'''

'''
    변수의 형변환
    1과 "11"은 다른 값 (정수 vs 문자열)
    11 > 2 ## True
    "11" > 2 ## TypeError: '>' not supported between instances of '
    "11" > "2" ## False
    int("11") > int("2") ## True
'''
## 문자열 변수
str_var = "This is my python code"
multi_line = """ I'm a developer.
I use python.
Thank you! """
print(str_var)
print(multi_line)

## 문자열 연산
integer_num1 = 12
integer_num2 = 34
str_num1 = "12"
str_num2 = "34"
print(integer_num1 + integer_num2)  # 46
print(str_num1 + str_num2)  # 1234
print(f"str_num1 * 3: {str_num1 * 3}")  # str_num1 * 3: 121212

## 인덱싱
str_var = "This is my python code."
print(f"str_var[11]: {str_var[11]}")  
print(f"str_var[-1]: {str_var[-1]}")  # 마지막 
print(f"str_var[-5]: {str_var[-5]}")  # 뒤에서 5번째

## slicing
print(f"str_var[11:17]: {str_var[11:17]}")  # python 17을 넣어야 16번째 글자까지 가져온다
print(f"str_var[11:-6]: {str_var[11:-6]}")  # 11번째부터 뒤에서 -6번째까지
print(f"str_var[:11]: {str_var[:10]}")  

## Method
print(f"str_var.isalpha(): {str_var.isalpha()}")  # False, 공백이 있어서
str_var = "Thisismypythoncode"
print(f"str_var.isalpha(): {str_var.isalpha()}")  # True,

num_var = "12"
print(f"num_var.isdecimal(): {num_var.isdecimal()}")  # True
num_var = "12.34"
print(f"num_var.isdecimal(): {num_var.isdecimal()}")  # False

str_var = "This is my python code."
print(f"str_var.upper(): {str_var.upper()}")  # 대문자로 변환
print(f"str_var.lower(): {str_var.lower()}")  # 소문자로 변
print(f"str_var.swapcase(): {str_var.swapcase()}")  # 대소문자 바꿈
print(f"str_var.replace('python', 'c++): {str_var.replace('python', 'c++')}")  # python을 c++로 바꿈
print(f"str_var.split(' '): {str_var.split(' ')}")  #

## Format String
weahter = "cloudy"
temp = 30.9
# 1) C-style formatting
str = "[%s / %.1f] Today's weather is %s and temperature is %.1f degrees." % (weahter, temp, weahter, temp)
print(f"1) C-style formatting: {str}")
# 2) str.format() method
str = "Today's weather is {} and temperature is {} degrees.".format(weahter, temp)
print(f"2-1) str.format() method: {str}")
str = "[{0} / {1}]Today's temperature is {1} degrees and weather is {0}.".format(weahter, temp)
print(f"2-2) str.format() method: {str}")
# 3) f-string (Python 3.6+)
str = f"Today 's weather is {weahter} and temperature is {temp} degrees."
print(f"3) f-string: {str}")

## 사용자로부터 입력 받기
num = input("Enter number: ")
print(f"num: {num}, type: {type(num)}")  # 입력은 항상 문자열로 받는다
num = int(num) + 1
print(f"num: {num}, type: {type(num)}")  # 정수로 변환