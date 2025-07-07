'''
    Module
    -. 파이썬 정의와 문장을 담고 있는 .py 파일
    -. import "모듈명"
    -. from "모듈명" import "개체명1", "개채명2" ,,,
    
    Package
    -. 모듈의 계층구조를 만드는 방법
    -. 모듈을 계층화하고, 모듈을 포함하는 디렉토리의 집합
    my_package
    + module1.py
    + module2.py
    + subpackage
    ++ __init__.py
    ++ module3.py 
    
    -. import package.module
    -. package.module.function()
    
    -. import package.module as alias
    -. alias.function()
    
    -. import package import *
    
    -. __init__.py
    -. 이 디렉토리가 파이썬 패키지임을 알려주는 파일
    -. 패키지 수준에서 사용되는 변수, 함수, 초기화 로직 정의
    -. 하위 모듈을 미리 로드하거나, 전역 변수 정의
    -. __all__: 참조하게 만들 모듈만 선택 가능 
'''
