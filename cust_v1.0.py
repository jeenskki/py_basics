from cust_func import data_func as mydf
from cust_func import print_func as mypf


class cust:
    def main(self):
        cust_list = []
        cust_list, page = mydf.load_cust(cust_list)

        while True:
            choice = mypf.print_menu()

            if choice == "I":
                page = mydf.input_cust(cust_list, page)

            elif choice == "C":
                mypf.print_c(cust_list, page)

            elif choice == "P":
                page = mypf.print_p(cust_list, page)

            elif choice == "N":
                page = mypf.print_n(cust_list, page)

            elif choice == "U":
                mydf.update_cust(cust_list)

            elif choice == "D":
                page = mydf.delete_cust(cust_list, page)

            elif choice == "Q":
                mydf.save_cust(cust_list)
                print("서비스를 종료합니다.")
                break
            else:
                print("메뉴를 잘못 선택하셨습니다.")


if __name__ == '__main__':
    client = cust()
    client.main()
