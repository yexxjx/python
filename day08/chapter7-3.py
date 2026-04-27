# p441
# 모듈 만들기: .py파일 만들기와 같다
# 1. xxxx.py 생성
# 2. 다른 .py 파일 내에서 import하여 모듈 호출하기

import test_module as test

# 다른 .py 파일에 존재하는 함수 호출
radius=test.number_input() 
print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# 프로그램의 진입점: __name__=="__main__"
print(__name__)

# p453
# 인터넷의 이미지 저장하기
from urllib import request
target=request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output=target.read()
print(output) # 바이너리 데이터로 반환, 앞에 b가 붙어있음
file=open("output.png","wb") # 바이너리 파일 저장시 "wb" 사용
file.write(output)
file.close()

