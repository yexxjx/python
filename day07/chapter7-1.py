# p401
# 모듈 호출 하기
# 표준 모듈: 파이썬 내장 라이브러리
# 외부 모듈: 설치형 라이브러리
# import 모듈명
# 특정한 변수/함수 가져오기 from 모듈명 import 가져오고싶은함수또는변수
# 모두 가져오기 from 모듈명 import *
# 식별자 부여 import 모듈명 as 식별자명

import math # import 모듈명
print(math.sin(1)) # 호출한 모듈에서 sin 함수 호출, .(접근연산자)
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))

from math import sin, cos, tan, floor, ceil
import math as m
print(m.sin(1))

# p407
# random 모듈
import random
print(random.random()) # 0.0 <= x < 1.0 난수 생성
print(random.uniform(10,20)) # uniform(시작 값, 끝 값) 실수
print(random.randrange(1,10)) # randrange(시작 값, 끝 값(까지 하고 싶으면 +1)) 정수
print(random.choice([2,9,4,20])) # choice([리스트]) 리스트 내 요소 랜덤 반환

# None
print(random.shuffle([2,9,4,20])) # shuffle([리스트]) 리스트 내 요소 랜덤 섞음

# 값 나옴
a=[2,9,4,20]
random.shuffle(a)
print(a)

print(random.sample([2,9,4,20], k=3)) # sample([리스트], k=n) 리스트 내 n개 반환