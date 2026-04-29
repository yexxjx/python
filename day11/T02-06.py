import numpy as np

# 1차원 배열 통계
x=np.array([1,2,3,4,5])

print(np.min(x)) # 최솟값
print(np.max(x)) # 최댓값
print(np.argmin(x)) # 최솟값의 (인덱스) 위치
print(np.argmax(x)) # 최댓값의 (인덱스) 위치
print(np.ptp(x)) # 최댓값-최솟값
print(np.sum(x)) # 총 합계
print(np.mean(x)) # 평균값
print(np.median(x)) # 중앙값
print(np.var(x)) # 분산: 요소들의 흩어진 정도
print(np.std(x)) # 표준편차: 분산의 양의 제곱근
print(np.sqrt(x)) # 루트

# 사분위수: 구역을 4개로 나눠서 데이터 분포의 위치 파악, q1: 제1사분위수, 
q1=np.percentile(x,25) # 1/4, 하위 25%
q3=np.percentile(x,75) # 3/4, 하위 75%
print(q1)
print(q3)
q2=np.percentile(x,50) # 1/2, 중앙값, 하위 50%
print(q2)
q4=q3-q1
print(q4)

# 2차원 배열 통계, 통계함수(x, axis=0(열기준)/1(행기준))
y=np.array([[1,2,3],[4,5,6]])
print(np.min(y))
print(np.min(y, axis=0)) # [1 2 3]
print(np.min(y, axis=1)) # [1 4]
print(np.argmin(y, axis=0)) # [0 0 0]
print(np.argmin(y, axis=1)) # [0 0]

print(np.max(y)) # 6 axis를 생략하면 2차원 배열을 평탄화(1차원으로 만들겠다는 의미)해서 통계를 구함
print(np.argmax(y, axis=0)) # [1 1 1]
print(np.argmax(y, axis=1)) # [2 2]

print(np.sum(y)) # 21
print(np.sum(y, axis=0)) # [5 7 9]
print(np.sum(y, axis=1)) # [ 6 15]

print(np.mean(y)) # 3.5
print(np.mean(y, axis=0)) # [2.5 3.5 4.5]
print(np.mean(y, axis=1)) # [2. 5.]

print(np.median(y)) # 3.5
print(np.median(y, axis=0)) # [2.5 3.5 4.5]
print(np.median(y, axis=1)) # [2. 5.]

print(np.var(y)) # 2.9166666666666665
print(np.var(y, axis=0)) # [2.25 2.25 2.25]
print(np.var(y, axis=1)) # [0.66666667 0.66666667]

print(np.std(y)) # 1.707825127659933
print(np.std(y, axis=0)) # [1.5 1.5 1.5]
print(np.std(y, axis=1)) # [0.81649658 0.81649658]