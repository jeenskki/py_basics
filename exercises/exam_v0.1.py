course = list()

def main():
    while True:
        print("""
            메인 메뉴
            1. 성적 입력
            2. 성적 출력
            3. 종료
            
            선택 >> """, end = "")
        m = int(input())
        
        if  m == 1:
            menu_1(course)
            
        elif m == 2:
            menu_2(course)
            
        elif m == 3:
            print("종료합니다.")
            break
        else:
            print("메뉴를 잘못 입력하셨습니다.")

def menu_1(c):
    print("성적 입력")
    
    for i in range(3):
        while True:
            c.insert(i, int(input("국어 %d : " % (i+1))))
            if 0 > c[i] or 100 < c[i]:
                print("국어 성적은 0~100점 사이의 점수를 입력해야 합니다.")
            else:
                break
    print("-"*40)

def menu_2(c):
    print("성적 출력")
    total = 0
    for i in range(3):
        total += c[i]
        
    avg = total / 3.0
    
    for i in range(3):
        print("[국어 %d : %3d] " % (i+1, c[i]), end = "")
    print("\n[총점 : %3d]" % total)
    print("[평균 : %6.2f]" % avg)
    print("-"*40)

if __name__ == '__main__':
    main()