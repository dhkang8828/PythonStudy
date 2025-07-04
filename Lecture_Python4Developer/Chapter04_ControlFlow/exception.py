'''
    예외 처리
    프로그램에서 발생할 수 있는 예외(오류) 상황을 처리하는 매커니즘
    
    try:
        value = int("abc")
    exception ValueError:
        print("Can't convert to integer")
    exception ZeroDivisionError:
        print("Can't divide by Zero")
    exception:
        print("Unknown Exception")
    else:
        print("Comple convert")
    finally: 
        print("Complete Program")
'''

while True:
    try:
        num1 = int(input("input first-value: "))
        num2 = int(input("input second-value: "))
        result = num1 / num2
        print(f"result of divide: {result}")
    except ValueError:
        print(f"ValueError has occured!")
        continue
    except ZeroDivisionError:
        print(f"ZeroDivisionError has Occured!")
        continue
    except:
        ## Exception을 그냥 내비두는 방법
        pass
    