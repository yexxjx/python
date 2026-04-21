# p316
# 튜플: () 소괄호 이용하여 여러 자료들을 감싸 자료형 단) 수정이 안 됨

# 튜플 선언
tuple_test=(10,20,30)
print(tuple_test)

# 요소 호출, 인덱스 사용
print(tuple_test[0])

# 주의할 점: 수정 안됨
# tuple_test[0]=40 # TypeError: 'tuple' object does not support item assignment

# p318
# 주의할 점2: 요소가 1개인 경우에는 쉼표 넣어준다
tuple_test2=(273,)

# 할당 구문: 오른쪽에 있는 리스트에 왼쪽 변수에 대입
[a,b]=[10,20]
print(a,b)
(c,d)=(10,20)
print(c,d)

# 튜플은 소괄호 생략 가능
tuple_test=10,20,30,40
print(tuple_test)

# p320
# 튜플을 이용한 스왑
a,b=10,20 # 10, 20 튜플을 할당 구문으로 a=10, b=20 대입
a,b=b,a
print(a,b)

# 함수 리턴 값
def test():
    return 10,20 # (10,20), [10,20], {'a': 10, 'b': 20}