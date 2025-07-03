'''
    조건문 
    알쥐? 
'''
    
# 날씨가 흐리고 강수확률이 70%이상이면 비가온다.
condition = "Sunny"
rain_rate = 0.799
if (condition == "Sunny") and (rain_rate >= 0.70):
    print(f"비올 확률이 높습니다")
elif (condition == "Cloudy"):
    print(f"날씨가 많이 흐립니다..")
elif (condition == "Sunny") and (rain_rate >= 0.70):
    print(f"my perdiction is alway good")
else:
    print(f"DRAM Support Oriantation")
    
## 사용자로부터 2개의 값을 입력 받느다.
## 첫 번째 값이 크다면 Win, 두 번째 값이 크다면 Lose를 출력
input_val1 = int(input("input first-value:"))
input_val2 = int(input("input second-value:"))
if (input_val1 > input_val2):
    print(f"Win")
elif (input_val1 < input_val2):
    print(f"Lose")
else:
    print(f"Draw")

## 시험 점수를 입력 받는다. 
## 1~99 이의의 값이 들어오면 종료
## A: 90~99, B: 80~89, C: 70~79 D: 60~69, F: ~59
score = int(input("input Score:"))
if ((score < 1) or (score > 99)):
    print("Wrong input value")
else:
    if score >= 90:
        print(f"A Grade")
    elif score >= 80:
        print(f"B Grade")
    elif score >= 70:
        print(f"C Grade")
    elif score >= 60:
        print(f"D Grade")
    else:
        print(f"F Grade")
        
## Refactoring
grade = ""
score = int(input("input score:"))
if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D"
elif score <= 59 and score >=1:
    grade = "F"
else:
    grade = None
if grade is not None:
    print(F"Grade is {grade}.")
    
