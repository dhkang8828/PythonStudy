'''
    Library
    -. 여러 모듈과 패키지의 모음
    -.함수, 클래스, 상수 등의 모음
    -. lib은 여러 패키지들의 묶음으루 구성된다. 
    
    표준 Library 
    -. 파일 입출력, 문자열 처리, 수학, 텍스트 처리
    https://docs.python.org/ko/3/library/index.html
    -. random
    -. math
    -. datetime
    -. os 
    -. ...
    
    외부 Library
    -. pip로 설치 (Package Installer for Python)
    python -m pip install SomePackage==1.0.4 
    python -m pip install "SomePackage>=1.0.4"
    
    라이브러리 버전 관리: Requirements.txt
    기본 설치: 모든 개발환경에 공통적으로 설치
    가상 환경: 해당 프로젝트에서만 사용되는 패키지 설치 
'''
import datetime
today = datetime.datetime.now()
print(f"today: {today}")

import random
rand_num = list()
for i in range(0, 10):
    rand_num.append(random.randint(0, 10))
for i in range(0, 10):
    print(f"rand_num[{i}]: {rand_num.pop(0)}")
    
basket = ["apple", "peach", "banana", "mango", "water-melon"]
print(f"choice: {random.choice(basket)}")

## @Terminal
## python3 -m venv my_env
## source my_env/bin/activate
## pip install requests
import requests
def get_example():
    response = requests.get("https://google.com")
    print(f"response: {response.text}")
if __name__ == "__main__":
    get_example()

