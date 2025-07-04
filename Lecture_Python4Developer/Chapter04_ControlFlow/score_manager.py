'''
    성적 관리 프로그램 
'''
students = {}

## 입력 대기창
while (True):
    ## 메뉴 출력 
    print("")
    print("1. 성적 입력")
    print("2. 학생 조회")
    print("3. 학점 조회")
    print("0. 종료")
    menu = input("input menu: ")

    ##1. 성적 입력
    if menu == "1":
        name = input("input student's name: ")
        score = input("input student's score: ")
        
        try:
            students[name] = int(score)
        except ValueError:
            print(f"Please enter Integer Value")
            continue
        print(f"{name}'s score {students[name]}")
               
    ##2. 학생 조희
    elif menu == "2":
        name = input("input student's name: ")
        if name in students.keys():
            print(f"{name}'s score: {students[name]}")
        else:
            print(f"{name} is not registered.")
            
    ##3. 학점 조회 
    elif menu == "3":
        name = input("input student: ")
        if name not in students.keys():
            print(f"{name} is not registered.")
            continue
        grade = ""
        score = students[name]
        if score >= 90 and score <=99:
            grade = "A"
        elif score >= 80 and score <=89:
            grade = "B"
        elif score >= 70 and score <= 79:
            grade = "C"
        elif score >= 60 and score <= 69:
            grade = "D"
        elif score >= 1 and score <= 59:
            grade = "F"
        else:
            grade = None
        
        if grade in ["A", "B", "C", "D"]:
            mod = score % 10
            if mod >= 5:
                grade = grade + "+"
        
        print(f"student {name}'s grade = {grade}")
    
    ##4. exit 
    elif menu == "0":
        break
    
    else:
        print("input menu is wrong")
        continue