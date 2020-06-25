import re
from datetime import datetime as dt

page = -1

def main():
    cust_list = []
    choice = print_menu()
    
    while True:
        if choice == "I":
            input_cust(cust_list)
        elif choice == "C":
            print_c(cust_list)
        elif choice == "P":
            pass
        elif choice == "N":
            pass
        elif choice == "U":
            pass
        elif choice == "D":
            pass
        elif choice == "Q":
            print("프로그램을 종료합니다.")
            break
        else:
            print("해당 메뉴는 존재하지 않습니다.")

    
def print_menu():
    return input ("""
                    다음 중 작업 하실 메뉴를 입력하세요
                    
                    I - 고객 정보 입력
                    C - 고객 정보 출력
                    P - 이전 고객 정보 출력
                    N - 다음 고객 정보 출력
                    U - 고객 정보 수정
                    D - 고객 정보 삭제
                    Q - 프로그램 종료
                    
                    >> """).strip().upper()

def input_cust(l):
     
    
    while True:
        name = input("이름을 입력하세요 : ")
        if name.isalpha() is True:
            break
        else:
            print("이름 형식이 맞지 않습니다.")
    
    while True:
        gender = input("성별을 입력하세요 (M / F) : ").upper()
        if gender in ("M", "F"):
            break
        else:
            print("성별 형식이 맞지 않습니다.")
        
    while True:
        email = input("이메일을 입력하세요 : ")
        if re.search(r'[\w+]+@[\w.+]+\.+[\w+]', email):
            break
        else:
            print("이메일 형식이 맞지 않습니다.")
            
    while True:
        birthyear = int(input("생년을 입력하세요 : "))
        if birthyear > dt.today().year:
            print("생일이 미래일 수 없습니다. 현재를 사세요.")
        else:
            break
    
    customer = {"name": name, "email": email, "gender": gender, "birthyear": birthyear}
    l.append(customer)
    page = len(l) - 1
    print("고객 정보가 성공적으로 저장되었습니다.")    

def print_c(l):
     
    if page >= 0:
        print("현재 고객 페이지 번호 : %d" % page)
        print(l[page])
    else:
        print("입력된 정보가 없습니다.")    

if __name__ == "__main__":
    main()