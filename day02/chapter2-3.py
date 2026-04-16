
# 변수: 하나의 자료 저정하는 (메모리) 공간
pi=3.141592 # = 같다 의미가 아니라 우변의 값을 좌변에 넣겠다

print(pi) # 변수 참조, 변수가 갖는 자료 반환
print(pi+pi)

print(pi+"입니다") # 오류 발생
print(pi,"입니다") # 연결

# 타입의 유연성=동적 타입, 단점: 타입 구분 어려움
# 자바 또는 c언어, int pi=3
# 파이썬, pi=3

# 복합 대입 연산자
number=100
number+=10
print(number) # 110
number-=10
print(number) # 100
number*=10
print(number) # 1000
number/=10
print(number) # 100
number%=3
print(number) # 1
number**=3
print(number) # 1

# 사용자 입력, input(), 주의할 점: 콘솔에 입력하는 구조로 무조건 *문자열*로 반환
input("인사말을 입력하세요>")
string=input("인사말을 입력하세요>")
print(string)
print(type(string)) # str

# 문자열을 숫자로 변환하기, 사용처: input, HTTP 문자열 통신(API, JSON 등) int() vs Integer.parseInt() vs parseInt()
# 타입 변환 해야 되는 이유: 자료 사용할 때 서로 다른 타입 간의 예외 발생
string_a=input("입력A > ")
int_a=int(string_a)
print(type(int_a))

string_b=int(input("입력B > ")) # 밥먹기(공부하기)
print(type(string_b)) 

string_c=float(input("입력C > "))
print(type(string_c))

# 숫자를 문자열로 바꾸기
pi=3.141592
string_d=str(pi)
print(type(string_d))

str_input=input("숫자입력>")
num_input=float(str_input)
print()
print(num_input, "inch")
print((num_input*2.54),"cm")