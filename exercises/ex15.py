class abc:
    b = 5                           # 클래스 변수
    def __init__(self, a):
        self.a = a                  # 인스턴스 변수

    def hello(self):
        print("hello")
# print(abc.a)
# print(abc.b)

hello = abc(1)
hello2 = abc(2)

hello2.b = 7

print(hello.b, hello2.b)

# print(hello.a, hello2.a)

# hello.a = 2
# hello2.a = 3

# print(hello.a, hello2.a)
# print(hello.hello(), hello2.hello())