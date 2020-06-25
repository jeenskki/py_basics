import re
from datetime import datetime as dt

page = -1

def main():
    cust_list = []
    
    while True:
        choice = input("""
        다음 중 작업 하실 메뉴를 입력 하세요.
        
        I - 고객 정보 입력
        C - 현재 고객 정보 출력
        P - 이전 고객 정보 출력
        N - 다음 고객 정보 출력
        U - 고객 정보 수정
        D - 고객 정보 삭제
        Q - 프로그램 종료
        
        >> """).strip().upper()
        
        if choice == "I":
            cust_list = cust_i(cust_list)
            
        elif choice == "C":
            cust_c(cust_list)
            
        elif choice == "P":
            cust_p(cust_list)
            
        elif choice == "N":
            cust_n(cust_list)
        
        elif choice == "U":
            cust_u(cust_list)
            
        elif choice == "D":
            cust_d(cust_list)
            
        elif choice == "Q":
            print("서비스를 종료합니다.")
            break
        else:
            print("메뉴를 잘못 선택하셨습니다.")
        
def cust_i (cl):
    global page
    
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
    cl.append(customer)
    page = len(cl) - 1
    print("고객 정보가 성공적으로 저장되었습니다.")
    return cl

def cust_c(l):
    global page
    if page >= 0:
        print("현재 고객 페이지 번호 : %d" % page)
        print(l[page])
    else:
        print("입력된 정보가 없습니다.")
    return

def cust_p(l):
    global page
    
    if page == -1 :
        print("입력된 정보가 없습니다.")
    elif page == 0 :
        print("가장 이전의 정보입니다.")
        print(l[page])
    else :
        page -= 1
        print("현재 고객 페이지 번호 : %d" % page)
        print(l[page])
        
        return

def cust_n(l):
    global page
    
    if page == -1:
        print("입력된 정보가 없습니다.")
    elif page == len(l) - 1:
        print("가장 최신의 정보입니다.")
        print(l[page])
    else:
        page += 1
        print("현재 고객 페이지 번호 : %d" % page)
        print(l[page])
        
    return
        
def cust_u(l):
    cName = input("수정할 고객의 이름을 입력해 주세요 : ")
    idx = -1
    for i, val in enumerate(l):
        if val["name"] == cName.strip():
            idx = i
            break
        
        if idx == -1:
            print("등록되지 않은 이름입니다.")
            break
        
    cKey = input("""
                 수정을 원하는 항목의 번호를 입력해주세요
                 (1: 이름, 2: 성별, 3: 이메일, 4: 생년, 기타: 돌아가기)
                 """)
    
    if cKey == "1":
        while True:
            new_name = input("수정할 이름을 입력하세요 : ")
            if new_name.isalpha() is True:
                l[idx]["name"] = new_name
                print("[{0}] 번 페이지의 [{1}] 항목이 [{2}] (으)로 변경되었습니다.".format(idx, "name", new_name))
                break
            else:
                print("이름이 형식에 맞지 않습니다.")
                
    elif cKey == "2":
        while True:
            new_gender = input("수정할 성별을 입력하세요 (M, F) : ").upper()
            if new_gender in ("M", "F"):
                l[idx]["gender"] = new_gender
                print("[{0}] 번 페이지의 [{1}] 항목이 [{2}] (으)로 변경되었습니다.".format(idx, "gender", new_gender))
            else:
                print("성별이 형식에 맞지 않습니다.")

    elif cKey == "3":
        while True:
            new_email = input("수정할 이메일을 입력하세요 : ")
            if re.search(r'[\w+]+@[\w.+]+\.+[\w+]', new_email):
                l[idx]["email"] = new_email
                print("[{0}] 번 페이지의 [{1}] 항목이 [{2}] (으)로 변경되었습니다.".format(idx, "email", new_email))
                break
            else:
                print("이메일이 형식에 맞지 않습니다.")
                
    elif cKey == "4":
        while True:
            new_bYear = int(input("수정할 생년을 입력하세요 : "))
            if new_bYear <= dt.today().year:
                l[idx]["birthyear"] = new_bYear
                print("[{0}] 번 페이지의 [{1}] 항목이 [{2}] (으)로 변경되었습니다.".format(idx, "birthyear", new_bYear))
                break
            else:
                print("생년이 형식에 맞지 않습니다.")            

def cust_d(l):
    global page
    
    if page == -1:
        print("삭제할 페이지가 없습니다.")
    else:
        while True:
            del_page = int(input("삭제할 페이지 번호를 입력해주세요 (0 ~ %d) : " % (len(l)-1)))
            if del_page < 0 or del_page >= len(l):
                print("잘못된 페이지 번호입니다.")
            else:
                break
        while True:
            confirm = input("정말 삭제하시겠습니까? (y/N) : ").upper()
            if confirm == "Y":
                del l[del_page]
                print("성공적으로 [%d] 번 페이지를 삭제했습니다." % del_page)
                if del_page == len(l) - 1:
                    page -= 1
                break
            elif confirm == "N":
                print("삭제를 취소합니다. 메인 메뉴로 돌아갑니다.")
                break
            else:
                print("메뉴를 잘못 선택하셨습니다.")
    
    return
                
if __name__ == '__main__':
    main()    