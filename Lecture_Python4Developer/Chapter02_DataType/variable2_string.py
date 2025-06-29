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


