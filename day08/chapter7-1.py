# p410
# OS 모듈

import os # 모듈 호출
print(os.name) # nt: 윈도우 뜻
print(os.getcwd()) # 현재 최상위 폴더 C:\Users\sku-102-05\Desktop\새 폴더\python
print(os.listdir()) # 현재 최상위 폴더의 내부 요소 ['.git', '.vscode', 'day01', 'day02', 'day03', 'day04', 'day05', 'day06', 'day07', 'day08']

os.mkdir("hello") # 폴더 생성
os.rmdir("hello") # 폴더 삭제

with open("./day08/original.txt", "w") as file:
    file.write("hello")
os.rename("./day08/original.txt", "new.txt") # 파일 이름 변경
os.remove("new.txt") # 파일 삭제

os.system("dir") # 시스템 명령어 실행

# p412
import datetime as a
print(a.datetime.now())
now=a.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
# 형식: Y년 m월 d일 H시 M분 S초
output_a=now.strftime("%Y-%m-%d %H:%M:%S")
print(output_a)

# p413
output=now.replace(year=(now.year+1), month=(now.month+1))
print(output)

# p414
# time 모듈
import time
print("3초간 일시 정지")
time.sleep(3) # 3초간 일시 정지, 스레드 일시 정지, 스레드란? 코드가 실행되는 흐름 단위
print("땡")

# p415
# urllib 모듈
from urllib import request # from 이용한 특정한 함수/변수만 가져오기
target=request.urlopen("https://google.com")
output=target.read()
print(output)

# p420
import os
def read_folder(path):
    output=os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(path+"/"+item)
        else:
            print("파일",item)
read_folder(".")