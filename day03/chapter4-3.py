# p231
# 범위: range
# [1] 숫자 1개만 넣는 경우, 0부터 n-1까지 리스트로 반환
print(list(range(5))) # [0, 1, 2, 3, 4]

# [2] 숫자 2개 넣는 경우, n부터 n-1까지 리스트로 반환
print(list(range(5,10))) # [5, 6, 7, 8, 9]

# [3] 숫자 3개 넣는 경우, n부터 n-1까지 n씩 증가하면서 리스트로 반환
print(list(range(0,10,2))) # [0, 2, 4, 6, 8]

# 반복문과 범위 활용
# for 반복변수 in range():
#   실행코드

# 예시1) 1부터 10까지 출력
for i in range(1,11):
    print(i)

# 예시2) 1부터 10까지 2씩 증가
for i in range(1, 11, 2):
    print(i)

# 예시3) 리스트와 범위 조합
array=[273, 32,103, 57, 52]
for index in range(len(array)): # 0부터 리스트의 마지막 인덱스까지
    print(array[index])

# 예시4) 역순 출력
for i in range(4, 0-1, -1): # 4부터 0까지 1씩 감소
    print(i)

for i in reversed(range(5)): # reversed(리스트), 리스트 역순으로 이터레이터(반복자/순회자) 제공
    print(i)
print(reversed(array))


for 단 in range(1,10):
    for 곱 in range(1,10):
        print(단*곱)


# p240
# 무한 반복
# while True: # 조건식에 True 대입했을 때 무한 반복
#     print(".", end="") # print(출력할 자료, end="") 줄 바꿈 처리하지 않음

# 1부터 10까지 출력
# i=1           # 반복 변수 초기값
# while 1<11:   # 반복 조건
#     print(i)
#     i+=1      # 반복 변수 증감식

# p242
# 리스트 활용
list_a=[1,2,1,2]
while 2 in list_a: # 만약에 2가 list_a에 포함되면
    list_a.remove(2) #2 삭제
    print(list_a)

# p244
# break 키워드
i=0                           # 초기값: 0부터
while True:                   # 무한반복조건
    print(i)
    i+=1                      # 증감식
    msg=input("종료할까요?> ") # 입력 받기
    if msg in ["Y", "y"]:     # 입력 받은 값이 Y/y 이면
        break                 # 가장 가까운 반복문 탈출

# p245
# continue 키워드
numbers=[5,15,6,20,7,25]
for number in numbers: # 반복문
    if number<10:      # 조건문
        continue       # 반복 변수가 10보다 작으면 다음으로 이동 
    print(number)


# p248
# [2]
key_list=["name","hp", "mp", "level"]
value_list=["기사", 200, 30, 5]
character={}
for i in range(0, len(key_list)):
    key=key_list[i]
    value=value_list[i]
    character[key]=value
print(character)

limit=10000
i=1

# [3]
sum_value=0
while True:
    sum_value+=1 # 누적 합계
    if(sum_value>limit): # 누적 합계가 10000보다 커지면
        break # 반복문 탈출
    i+=1 # 1씩 증가
    print(i, sum_value)

# [4]
max_value=0
a=0
b=0
for i in range(1, 51): # 1부터 50까지 1씩 증가 반복
    j=100-i #
    if max_value<i*j:
        max_value=i*j
        a=j
        b=i
        print(a,b,max_value)