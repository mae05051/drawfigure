def left_jikgak(): #좌측 직각 삼각형 함수
    x=int(input("10이하의 높이를 입력하세요: "))
    if x<=10:
        print()
        for i in range(1,x+1):
            for j in range(x+1-i):
                print("*",end="")
            print()
    else: #높이가 10을 초과하면 다시 입력받음(도형의 높이를 10이하로 제한)
        print("높이가 10을 초과하였습니다. 다시 입력하세요.\n")
        left_jikgak()

def right_jikgak(): #우측 직각 삼각형 함수
    x=int(input("10이하의 높이를 입력하세요: "))
    if x<=10:
        print()
        for i in range(x):
            for j in range(x):
                if j < i:
                    print(' ', end='')
                else:
                    print('*', end='')
            print()
    else: #높이가 10을 초과하면 다시 입력받음(도형의 높이를 10이하로 제한)
        print("높이가 10을 초과하였습니다. 다시 입력하세요.\n")
        right_jikgak()

def isoscele(): #이등변 삼각형 함수
    x=int(input("10 이하의 높이를 입력하세요: "))
    if x<=10:
        print()
        for i in range(x, 0, -1):
            print(" "*(x-i), "*"*(2*i-1))

    else: #높이가 10을 초과하면 다시 입력받음(도형의 높이를 10이하로 제한)
        print("높이가 10을 초과하였습니다. 다시 입력하세요.\n")
        isoscele()


def triangle(): #삼각형 함수
    print("삼각형의 종류를 선택하세요.")
    print("1. 좌측 직각삼각형")
    print("2. 우측 직각삼각형")
    print("3. 이등변 삼각형")
    samgak=int(input(">> "))
    print()
    if samgak==1: #1번을 입력받았을 때(좌측 직각삼각형)
        left_jikgak() #좌측 직각 삼각형 함수
    elif samgak==2: #2번을 입력받았을 때(우측 직각삼각형)
        right_jikgak() #우측 직각 삼각형 함수
    elif samgak==3: #3번을 입력받았을 때(이등변 삼각형)
        isoscele() #이등변 삼각형 함수
    else: #1,2,3 외 다른 숫자가 입력된 경우 -> 다시 함수 실행
        print("잘못된 입력입니다. 다시 입력하세요.\n")
        triangle()   

def left_parallelogram(): #좌측 평행사변형 함수
    a=int(input("10이하의 높이를 입력하세요: "))
    b=int(input("10이하의 너비를 입력하세요: ")) #a가 높이 b가 너비
    if a > 10 or b > 10:
        print("높이나 너비가 10을 초과하였습니다. 다시 입력하세요.\n")
        left_parallelogram() 
    else:
        print()
        for i in range(1, a+1):
           print(' ' * i + '*' * b + ' ' * (a+1-i))
          
def right_parallelogram(): #우측 평행사변형 함수
    a=int(input("10이하의 높이를 입력하세요: "))
    b=int(input("10이하의 너비를 입력하세요: ")) #a가 높이 b가 너비
    if a > 10 or b > 10: #높이나 너비가 10을 초과하면 다시 입력받음(도형의 높이와 너비를 10이하로 제한)
        print("높이나 너비가 10을 초과하였습니다. 다시 입력하세요.\n")
        right_parallelogram() 
    else:
        print()
        for i in range(1, a+1):
           print(' ' * (a+1-i) + '*' * b + ' ' * i)

def diamond(): #마름모 함수
    x=int(input("10이하의 홀수의 높이를 입력하세요: "))
    a=int((x+1)/2)
    if x>10: #높이나 너비가 10을 초과하면 다시 입력받음(도형의 높이와 너비를 10이하로 제한)
        print("높이가 10을 초과하였습니다. 다시 입력하세요.\n")
        diamond() 
        
    elif x%2==0: #마름모의 높이가 짝수일 때 다시 입력받음
        print("짝수를 입력하셨습니다. 다시입력하세요.\n")
        diamond() 
    else:
        print()
        for i in range(1, a+1):
            print(" "*(a-i), "*"*(2*i-1))
        for i in range(a-1, 0, -1):
            print(" "*(a-i), "*"*(2*i-1))

def quadrangle(): #사각형 함수
    print("사각형의 종류를 선택하세요.")
    print("1. 좌측 평행사변형")
    print("2. 우측 평행사변형")
    print("3. 마름모")
    sagak=int(input(">> "))
    print()
    if sagak==1: #1번을 입력받았을 때(좌측 평행사변형)
        left_parallelogram()
    elif sagak==2: #2번을 입력받았을 때(우측 평행사변형)
        right_parallelogram()
    elif sagak==3: #3번을 입력받았을 때(마름모)
        diamond()
    else: #1,2,3 외 다른 숫자가 입력된 경우 -> 다시 함수 실행
        print("잘못된 입력입니다. 다시 입력하세요.\n")
        quadrangle()

def mainfuction(): #최초 화면
    print()
    print("도형을 선택하세요.")
    print("1. 삼각형")
    print("2. 사각형")
    print("3. 종료")
    choice=int(input(">> "))
    print()
    if choice==1: #1번 선택시
        triangle() #삼각형 함수 실행
        mainfuction() #삼각형을 만들고 다시 최초화면
    elif choice==2: #2번 선택시
        quadrangle() #사각형 함수 실행
        mainfuction() #사각형을 만들고 다시 최초화면
    elif choice==3: #3번 선택시
        print("프로그램이 종료되었습니다.")
        exit() #프로그램 종료
    else:#1, 2, 3외의 숫자를 입력했을 때
        print("\n잘못된 입력입니다. 다시 입력하세요.\n")
        mainfuction() #다시 최초화면         

mainfuction()