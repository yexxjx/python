# p164
# 파이썬 조건문, if 조건:
number=int(input("정수 입력: "))

if number>0:
    print("양수입니다.")
if number<0:
    print("음수입니다.")
if number==0:
    print("0입니다.")


number=input("정수 입력>")
number=int(number)

if number%2==0:
    print("짝수입니다.")
if number%2==1:
    print("홀수입니다.")


# p180
# if~else
number=int(input("정수 입력: "))
if number%2==0:
    print("짝수")
else:
    print("홀수")


# if~ elif~ elif~ else
if number%2==0:
    print("짝수")
elif number%2==1:
    print("홀수")
else:
    print("잘못된 값")

# 조건 3개 이상: [1] if if if [2] if ~ elif