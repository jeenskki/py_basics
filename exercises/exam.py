course = list()

while True:
    print("""
          메인 메뉴
          1. 성적 입력
          2. 성적 출력
          3. 종료
          
          선택 >> """, end = "")
    menu = int(input())
    
    if menu == 1:
        print("성적 입력")
        
        for i in range(3):
            while True:
                course.insert(i, int(input("국어 %d : " % (i+1))))
                if 0 > course[i] or 100 < course[i]:
                    print("국어 성적은 0~100점 까지의 점수를 입력해야 합니다.")
                if 0 <= course[i] and 100 >= course[i]:
                    break
        print("-"*40)
        
    elif menu == 2:
        print("성적 출력")
        total = 0
        for i in range (3):
            total += course[i]
            
        avg = total / 3.0
        
        for i in range (3):
            print("[국어 %d : %3d] " % (i+1, course[i]), end="")
        print("\n[총점 : %3d ] " % total)
        print("[평균 : %6.2f")
        
    elif menu == 3:
        print("종료합니다.")
        break

    else:
        print("메뉴가 올바르지 않습니다.")
    