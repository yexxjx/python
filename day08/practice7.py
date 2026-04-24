# [ Python Practice7 종합예제]

# 경기도 아파트 실거래가 조회 시스템 ( 리스트와 딕셔너리 사용 )
# 데이터 출처: 국토교통부 실거래가 공개시스템(경기도 최근 1년치 아파트 매매 데이터) 
# https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

# 주요 기능 요구사항
# 1. 데이터 저장 및 로드 (파일 처리)
#     users.txt: 회원 정보 저장 (식별번호,아이디,비밀번호,이름) 직접 생성 
#     아파트(매매)_실거래가_20260424091956.csv: 직접 다운로드한 실거래가 데이터 파일

# 2. 사용자 기능 (로그인 후 이용 가능)
#     2-1) 공통 : 
#       - 회원가입, 
#       - 로그인
#       - 로그아웃
#     2-2) 회원 전용 메뉴: ( 어려운분들은 구현 안해도 됩니다. )
#       - 지역명 검색: '시군구' 열에서 사용자가 입력한 지역명(예: "만안구", "평촌동")이 포함된 모든 거래 내역 출력
#       - 금액 범위 검색: 사용자가 입력한 '최소 금액'과 '최대 금액' 사이의 거래 내역 필터링 출력
#       - 전체 통계 조회: 전체 데이터의 평균 거래가 등 간단한 통계 정보 출력

import json
data=[{"uno":"1", "uid":"U001", "upwd":"0001", "uname":"user01"},
        {"uno":"2", "uid":"U002", "upwd":"0002", "uname":"user02"},
        {"uno":"3", "uid":"U003", "upwd":"0003", "uname":"user03"},
        {"uno":"4", "uid":"U004", "upwd":"0004", "uname":"user04"},
        {"uno":"5", "uid":"U005", "upwd":"0005", "uname":"user05"}]
file_path="./day08/users.txt"
with open(file_path, "w") as file:
    json.dump(data, file, indent=4)

import csv
with open(r"C:\Users\sku-102-05\Desktop\새 폴더\python\day08\아파트(매매)_실거래가_20260424151649.csv", "r", encoding='UTF-8') as file:
    csv_reader=csv.reader(file)
    for row in csv_reader:
        print(row)

def login():
    users={}
    with open("./day08/users.txt", "r") as file:
        for line in file:
            uid, upwd=line.strip().split(":")
            users[uid]=upwd

    id_input=input("아이디 입력> ")
    pwd_input=input("비밀번호 입력> ")

    if id_input in data and data[id_input]==pwd_input:
        print("로그인 성공")
    else:
        print("로그인 실패")
print(login())



