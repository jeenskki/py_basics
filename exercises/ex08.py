j = True
while j:
    command = input('''
    I : 입력 화면 이동
    R : 조회 화면 이동
    D : 삭제 화면 이동
    Q : 종료''')
    
    if command is "I":
        print("입력 화면 입니다.")
    if command is "R":
        print("조회 화면 입니다.")
    if command is "D":
        print("삭제 화면 입니다.")
    if command is "Q":
        j = False
