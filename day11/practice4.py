# customer_purchase_data.csv 다운로드 받아서 현재 py 파일과 같은 폴더에 저장
import numpy as np

# 1. .csv(, 쉼표로 구분한 자료의 형식) 파일 가져오기
# data=np.genfromtxt("파일경로", delimiter='구분문자', skip_header=제외할헤더(행)수)
data=np.genfromtxt(
    "./day11/customer_purchase_data.csv",
    delimiter=",",
    skip_header=1)
# 2. 가져온 데이터의 넘파이 형식 확인
print(data.shape) # (1000, 5)

# 1. 데이터 준비 : 데이터 구조 (Columns)
# [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
# [고객ID, 방문횟수, 체류시간, 장바구니횟수, 구매금액]

# 2. 프로젝트 단계별 미션
# Step 1: 데이터 기초 통계 분석
# 전체 데이터에서 구매 금액(마지막 열)만 추출하여 sales 배열을 만드세요.
sales=(data[: , 4])
print(sales)

# 고객들의 평균 구매 금액과 총 매출액을 계산하여 출력하세요.
print("평균:", np.mean(sales), "총 매출액:", np.sum(sales))

# Step 2: 충성 고객 필터링 (Boolean Indexing)
# 방문 횟수(1번 열)가 20회 이상이거나 구매 금액이 2000달러 이상인 고객을 '충성 고객'으로 분류하
# 세요.
con1=(data[: ,1]>=20)
con2=(data[: ,4]>=2000)
result=data[con1|con2]

# 충성 고객들의 ID를 추출하여 출력하세요.
print(result[: ,0])

# Step 3: 구매 전환율 및 효율성 계산 (Broadcasting)
# 구매금액 / 방문횟수를 계산하여 방문당 평균 매출(ARPV) 배열을 생성하세요.
ARPV=(data[: ,4])/(data[: ,1])

# ARPV가 가장 높은 고객의 ID를 출력하세요.
print(np.max(ARPV))
findId=(np.argmax(ARPV)) # 인덱스 위치를 알려줌
print(data[findId,0])

# Step 4: 휴면 고객 및 이탈 위험군 식별 (Logic)
# 방문 횟수가 3회 이하이면서 장바구니에 담은 횟수가 1회 이하인 고객을 '이탈 위험 고객'으로 분류합
# 니다. 
result=(data[: ,1]<=3)&(data[: ,3]<=1)

# 이 조건에 해당하는 고객들의 데이터를 추출하고, 전체에서 몇 명인지 출력하세요. (조건 True의 개수를 세는 것과 같음)
print(np.sum(result))

# Step 5: 고객 등급 정규화( (가격-최솟값)/(최댓값-최솟값) ) 및 VVIP 선정 (Normalization)
# 정규화하는 이유: 어떠한 자료들을 0과 1 사이의 값으로 만들어서(백분율), 비교가 쉽다(용이하다), 속도 빠르다
# 구매 금액 데이터를 0과 1 사이의 값으로 정규화(Min-Max Scaling) 하세요.
data_min=np.min(data[:,4])
print(data_min)
data_max=np.max(data[:,4])
print(data_max)

# 정규화된 값이 0.9 이상인 고객을 'VVIP'로 정의하고, 해당 고객들의 모든 정보(Row 전체)를 출력하
# 세요.
norm_data=(sales-data_min)/(data_max-data_min)
vip_data=norm_data>=0.9
print(vip_data)
print(data[vip_data])

# 예시
x=np.array([True, False, True])
y=np.array([1,2,3])
print(y[x]) # [1 3]