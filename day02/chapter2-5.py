# p157
# 비교 연산자: ==같다 !=다르다 >크다 <미만 >=크거나같다 <=작거나같다
# 문자열 비교: 가나다/abc 순으로 앞에 있는 것이 작은 값
print("가방"=="가방") # True
print("가방"!="하마") # True 
print("가방"<"하마") # True
print("가방">"하마") # False "가"랑 "하"를 유니코드로 표현했을 때 "하"가 더 큼

# p158
# 범위 논리
x=25
print(20<x<30)
print(40<x<60)

# p159
# 논리 연산자: and 이면서/그리고/모두 or 또는/이거나 not 부정/반대 vs && || !
print(not True) # False
print(not False) # True

# p160-161
print(True and True) # True
print(True and False) # False
print(True or True) # True
print(True or False) # True