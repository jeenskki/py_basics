def print_menu():
    return input("""
        다음 중 작업 하실 메뉴를 입력 하세요.
        
        I - 고객 정보 입력
        C - 현재 고객 정보 출력
        P - 이전 고객 정보 출력
        N - 다음 고객 정보 출력
        U - 고객 정보 수정
        D - 고객 정보 삭제
        Q - 프로그램 종료
        
        >> """).strip().upper()
    
def  print_c (l, p):
     
    if p >= 0:
        print("현재 고객 페이지 번호 : %d" % p)
        print(l[p])
    else:
        print("입력된 정보가 없습니다.")
    return

def  print_p (l, p):
     
    if p == -1 :
        print("입력된 정보가 없습니다.")
    elif p == 0 :
        print("가장 이전의 정보입니다.")
        print(l[p])
    else :
        p -= 1
        print("현재 고객 페이지 번호 : %d" % p)
        print(l[p])
        
    return p

def  print_n (l, p): 
    
    if p == -1:
        print("입력된 정보가 없습니다.")
    elif p == len(l) - 1:
        print("가장 최신의 정보입니다.")
        print(l[p])
    else:
        p += 1
        print("현재 고객 페이지 번호 : %d" % p)
        print(l[p])
        
    return p    