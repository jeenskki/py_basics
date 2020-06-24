# 이메일 검사를 위한 정규식 불러오기
import re

cust_list = []
page = -1

# 이메일 검사 변수 생성
mailCheck= re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

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
    """)
    
    # 메뉴 input 대/소문자 전부 사용 가능하게
    if choice in ("I", "i"):
        # print("고객 정보 입력 로직")    
        customer = {"name": "","gender": "","email": "", "birthyear": 0}
        while True:
            name = input("이름을 입력 하세요: ")
            # 이름에 숫자나 특수문자가 있는지 확인
            if name.isalnum() is True and name.isalpha() is True:
                break
            else:
                print("잘못된 이름입니다. 다시 입력해주세요")
                
        while True:
            gender = input("성별을 입력 하세요 (M/F): ")
            if gender in ("M", "F"):
                break
            else:
                print("오류 : 성별은 M 또는 F로 기입해주세요.")
                
        while True:        
            email = input("이메일 주소를 입력 하세요 : ")
            # 이메일 검사
            if (mailCheck.match(email) != None) is True:
                break
            else:
                print("오류 : 이메일을 양식에 맞게 기입해주세요.")
        
        while True:
            birthyear = input("출생 년도를 입력 하세요 : ")
            # 생년이 숫자로 입력되었는가 확인
            if birthyear.isdigit() is True:
                break
            else:
                print("오류 : 생년을 양식에 맞게 기입해주세요.")
        
        customer["name"] = name
        customer["birthyear"] = birthyear
        customer["gender"] = gender
        customer["email"] = email
        
        cust_list.append(customer)
        page = len(cust_list) -1
        
    elif choice in ("C", "c"):
        # print("현재 고객 정보 출력")
        if page >= 0:
            print("현재 고객 페이지 번호 : %d" % page)
            print(cust_list[page])
        else:
            print("입력된 정보가 없습니다.")
            
    elif choice in ("P", "p"):
        
        if page == -1:
            print("입력된 정보가 없습니다.")
        elif page == 0:
            print(cust_list[page])
            print("가장 이전의 정보입니다.")
        else:
            page -= 1
            print(cust_list[page])
    
    elif choice in ("N", "n"):
        
        if page == -1:
            print("입력된 정보가 없습니다.")
        elif page == len(cust_list) - 1:
            print(cust_list[page])
            print("가장 최근의 정보입니다.")
        else:
            page += 1
            print(cust_list[page])
            
    elif choice in ("U", "u"):
        if page == -1 :
            print("수정 할 정보가 없습니다.")
        else:
            while True:
                page = int(input("수정을 원하는 페이지를 입력해주세요."))
                if page < 0 or page >= len(cust_list):
                    print("해당 페이지는 존재하지 않습니다.")
                else:
                    break
                
            key = input("수정을 원하는 항목의 번호를 입력해주세요 (1: 이름, 2: 성별, 3: 이메일, 4: 생년) : ")
            if key is "1":
                while True:
                    cust_list[page]["name"] = input("이름을 입력 하세요: ")
                    if cust_list[page]["name"].isalnum() is True and cust_list[page]["name"].isalpha() is True:
                        break
                    else:
                        print("잘못된 이름입니다. 다시 입력해주세요")
                
            elif key is "2":
                while True:
                    cust_list[page]["gender"] = input("수정할 성별을 입력해 주세요(M/F) : ")
                    if cust_list[page]["gender"] in ("M", "F"):
                        break
                    else:
                        print("성별이 잘못 입력되었습니다.")
                print(cust_list[page]["gender"], end="")
                print("(으)로 수정되었습니다.")
                
            elif key is "3":
                while True:
                    cust_list[page]["email"] = input("새로 수정할 이메일을 입력하세요 : ")
                    if (mailCheck.match(cust_list[page]["email"]) != None) is True:
                        break
                    else:
                        print("이메일 양식이 올바르지 않습니다.")
                print(cust_list[page]["email"], end="")
                print("(으)로 수정되었습니다.")
                
            elif key is "4":
                while True:
                    cust_list[page]["birthyear"] = int(input("새로 수정할 생년을 입력해주세요 : "))
                    if cust_list[page]["birthyear"].isdigit() is True:
                        print(cust_list[page]["birthyear"], end="")
                        print("(으)로 수정되었습니다.")
                        break
                    else:
                        print("입력된 생년이 양식에 맞지 않습니다.")
            else:
                print("잘못 입력하셨습니다. 메인 메뉴로 돌아갑니다.")

    elif choice in ("D", "d"):
        if page == -1 :
            print("삭제할 페이지가 없습니다.")
        else :
            while True:
                page = int(input("삭제할 페이지 번호를 입력해주세요 : "))
                if page < 0 or page >= len(cust_list):
                    print("잘못된 페이지 번호입니다.")
                else:
                    break
            while True:
                confirm = input("정말 삭제하시겠습니까? (Y/N)")
                if confirm in ("Y", "y"):
                    del cust_list[page]
                    print("성공적으로 %d 번 페이지가 삭제되었습니다." % page)
                    break
                elif confirm in ("N", "n"):
                    print("삭제가 취소되었습니다. 메인 메뉴로 돌아갑니다.")
                    break
                else:
                    print("잘못된 키 입력입니다.")
    
    elif choice in ("Q", "q"):
        print("시스템을 종료합니다.")
        break
    
    else:
        print("메뉴를 잘못 선택하셨습니다.")