'''
    할일 목록 관리자
    -. 사용자로부터 입력을 받아, 할 일 목록을 정리
    -. 추가, 삭제, 목록 조회
'''

todo_list = list()

while True:
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 조회")
    print("4. 종료")
    
    choice = input("원하는 작업을 선택하세요 (1-4): ")
    
    if choice == '1':
        task = input("추가할 할 일을 입력하세요: ")
        todo_list.append(task)
        print(f"'{task}'이(가) 추가되었습니다.")
        pass
        
    elif choice == '2':
        task = input("삭제할 할 일을 입력하세요: ")
        if task not in todo_list:
            print(f"'{task}'은(는) 목록에 없습니다")
            continue
        todo_list.remove(task) 
        print(f"'{task}'이(가) 삭제되었습니다.")
        pass
        
    elif choice == '3':
        print("할 일 목록을 조회합니다...")
        print(todo_list)
        pass
        
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다. 다시 시도하세요.")