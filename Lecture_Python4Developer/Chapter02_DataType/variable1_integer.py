'''
    데이터 타입
    정수형 데이터
    1. python3는 최대/최소값이 따로 없다
    2. 사칙연산(+, -, *, /, //, %, **)
    3. 비교연사s(==, !=, >, <, >=, <=)
    4. 비트연산자(&, |, ^, ~, <<)
    5. 논리연산자(and, or, not)
    
    실수형 데이터
    1. 부동소수점을 통한 실수 표현
    2. 사칙연산(+, -, *, /, //, %, **)
    3. 기본적으로 정수형 데이터와 동일
    
    Boolean 데이터
    1. True, False
    2. 논리연산자(and, or, not)
    3. True and True = True
    4. True and False = False
    5. True or True = True
    6. True or False = True
    7. False and False = False  
''' 

## 변수의 선언
integer_variable = 42
print(f"integer_variable: {integer_variable}")

var = 10
print(f"var + 10: {var + 10}")  # 덧셈
print(f"var - 10: {var - 10}")  # 뺄
print(f"var / 10: {var / 10}")  # 나눗셈
print(f"var * 10: {var * 10}")  # 곱셈
print(f"var // 10: {var // 10}")  # 몫
print(f"var % 10: {var % 10}")  # 나머지
print(f"var ** 2: {var ** 2}")  # 제곱

## 변수 대입
var2 = var / 2
print(f"var2: {var2}")

## 대소 비교
print(f"var: {var} var2 = {var2}")  # 같음
print(f"var == var2: {var == var2}")  # 같음
print(f"var > var2: {var > var2}")    # 큼

## 
var_float = 3.14
print(f"var_float: {var_float}")
print(f"var_float * 6: {var_float * 6}")  #
print(f"var_float / 2: {var_float / 2}")  # 나눗셈

## 사칙연산 우선 순위
result = var * 10 + 5
print(f"result: var * 10 + 5: {result}")  # 곱셈이 덧셈
result = 5 + (var * 10)
print(f"result: 5 + (var * 10): {result}")  # 괄호가 우선
result = (5 + var) * 10
print(f"result:(5 + var) * 10 {result}")  # 괄호가 우선   

## 논리 연산
is_true = True
is_false = False
print(f"is_true: {is_true}, is_false: {is_false}")
print(f"is_true and is_false: {is_true and is_false}")  # 논리 연산
print(f"is_true or is_false: {is_true or is_false}")  # 논리 연산
print(f"not is_true: {not is_true}")  # 논리 연산
print(f"not is_false: {not is_false}")  # 논리