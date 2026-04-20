# p292
# 재귀함수란? 현재 실행 중인 (자신의) 함수를 다시 호출하는 것
# [1] 반복문으로 팩토리얼 구하기
def func1(n):
    output=1
    for i in range(1, n+1):
        output*=i
    return output
print("5팩토리얼:", func1(5)) # 5팩토리얼: 120

# [2] 재귀함수로 팩토리얼 구하기
# func2(5) >    5*재귀 (안끝남) 5*4*3*2*1*1
# func2(4) >        5*재귀 (안끝남) 4*3*2*1*1
# func2(3) >            5*재귀 (안끝남) 3*2*1*1
# func2(2) >                5*재귀 (안끝남) 2*1*1
# func2(1) >                    5*재귀 (안끝남) 1*1
# func2(0) >                        return 1 (fun2 함수는 몇 번 호출? 6번 호출, return 6번 되어야 함)

def func2(n):
    if n==0: # 만약에 매개변수가 0이면
        return 1 # 함수 종료
    else:
        return n*func2(n-1) # 재귀함수 호출
print("5!:", func2(5)) # 120

# p295
# [3] 피보나치 수열1, 1번째 수열: 1, 2번째 수열: 2, n번째 열: n-1수열+n-2수열
    # func3(4) > return 재귀(3)+재귀(2)
    #   func3(3)  > return 재귀(2)+재귀(1)
    #       func3(2)  > return 재귀(1)+재귀(0)
# 문제점: 재귀수가 많아서 계산식이 오래 걸림
counter2=0
def func3(n):
    global counter2
    counter2+=1
    print("-----", counter2)
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return func3(n-1)+func3(n-2)
print(func3(10))

# [4] 피보나치 수열2, 메모화
dictionary={ # 결과를 저장하는 딕셔너리
    1:1, 2:1, 
}

counter=0  # 함수 밖 변수
def func4(n):
    global counter # 함수 밖에 있는 변수 호출
    counter+=1
    print("-----", counter)
    if n in dictionary: #만약에 매개변수가 dictionary에 존재하면 
        return dictionary[n] # 저장/메모된 값을 리턴
    else:
        output=func4(n-1)+func3(n-2) # 피보나치 수열 공식
        dictionary[n]=output # 결과 메모/저장
        return output #반환
print(func4(5))

# p315
앉힐수있는최소사람수=2
앉힐수있는최대사람수=10
전체사람의수=6
memo={}

def 문제(남은사람수, 최소사람수):
     key=str([남은사람수, 최소사람수])
     # 종료 조건
     if key in memo:
         return memo[key]
     if 남은사람수<0:
         return 0
     if 남은사람수==0:
         return 1
     
     # 재귀 처리
     count=0 # 인원 수
     for i in range (최소사람수, 앉힐수있는최대사람수+1): # 2부터 10까지 1씩 증가 반복 
         count+=문제(남은사람수-i,i) # 남은사람수에 i만큼 제외하고, i 대입
     memo[key]=count
     return count
print(문제(전체사람의수,앉힐수있는최소사람수))