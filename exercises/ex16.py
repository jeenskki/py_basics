class exam:
    kor_c = 0                                  # 클래스 변수
    __kor_c = 0                                # 비공개 클래스 변수

    def __init__ (self, kor):
        self.kor_i = kor                       # 인스턴스 변수
        self.__kor_i = kor                     # 비공개 인스턴스 변수

    def set_kor_c(self, kor_c):
        exam.kor_c = kor_c

    def set_kor_i(self, kor_i):
        self.__kor_i = kor_i

    def get_kor_i(self):
        return self.__kor_i

temp_exam = exam(100)
temp_exam1 = exam(90)
print(temp_exam.kor_i, temp_exam1.kor_i)
# print(temp_exam.kor_c)

# temp_exam.kor_c = 100
temp_exam.set_kor_c(100)

# print(temp_exam.kor_c, temp_exam1.kor_c)
temp_exam.set_kor_i(90)
print(temp_exam.get_kor_i())

