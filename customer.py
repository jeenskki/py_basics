cust_list = []
page = -1
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
    
    if choice is "I":
        customer = {"name": '', "gender": '', "email": '', "birthyear": ''}
        customer["name"] = input("Please enter customer's name : ")
        customer["gender"] = input("Please enter customer's gender : ")
        customer["email"] = input("Please enter customer's email : ")
        customer["birthyear"] = input("Please enter customer's birthyear : ")
        cust_list.append(customer)
        print()
        print("Customer Data Input Completed.")
    elif choice is "C":
        page = len(cust_list) -1
        print(cust_list[page])
    elif choice is "P":
        if page == -1:
            page = len(cust_list) -2
            print(cust_list[page])
        elif page == 0:
            print("Already reached the first customer.")
            print("Thus, you will see the first customer's data.")
            print(cust_list[page])
        else:
            page -= 1
            print(cust_list[page])
    elif choice is "N":
        if page == len(cust_list)-1:
            print("Already reached the last customer.")
            print("Thus, you will see the last customer's data")
            print(cust_list[page])
        elif page == -1:
            page = len(cust_list) -1
            print("가장 최근에 추가된 고객의 정보를 확인합니다.")
            print(cust_list[page])
        else:
            page += 1
            print(cust_list[page])
    elif choice is "U":
        change_list = []
        change_page = 0
        page = int(input("Enter the page you wish to change: "))
        customer["name"] = input("Please enter customer's name : ")
        customer["gender"] = input("Please enter customer's gender : ")
        customer["email"] = input("Please enter customer's email : ")
        customer["birthyear"] = input("Please enter customer's birthyear : ")
        change_list.append(customer)
        cust_list[page] = change_list[change_page]
        change_page += 1
        print(cust_list[page])
    elif choice is "D":
        page = int(input("Enter the page index you wish to delete: "))
        if page < 0 or page > len(cust_list):
            print("Invalid Page Number.")
        else:
            del cust_list[page]
            page = len(cust_list) - 1
        print("Page is successfully deleted. Page reset to the top")
    elif choice is "Q":
        break
    else:
        print("Invalid Menu.")
        print()
    