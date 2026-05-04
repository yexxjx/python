import pandas as pd
# 판다스
# pd.Series # 1차원
# pd.DataFrame # 2차원

# [1] 데이터프레임 생성, pd.DataFrame(2차원리스트,colums=[열이름목록])
data_list=[ # 2차원 리스트
    ["ant",25,"seoul"],
    ["bee",30,"busan"],
    ["cat",35,"incheon"]]
x=pd.DataFrame(data_list,columns=["name","age","city"])
print(x)

# [2] 데이터프레임 생성2, pd.DataFrame(딕셔너리), 대부분의 공공자료는 딕셔너리
data_dict={"name":["ant","bee","cat"], 
           "age":[25,30,35], 
           "city":["seoul","busan","incheon"]} # 딕셔너리
x=pd.DataFrame(data_dict)
print(x)

# [3] 데이터프레임 생성3, pd.DataFrame(넘파이배열, colums=[열이름])
import numpy as np
data_np=np.array(data_list)
x=pd.DataFrame(data_np, columns=["name","age","city"],index=["a","b","c"])
print(x)

# [4] 주요 탐색
print(x.shape) # 행/열 크기
print(x.columns) # 컬럼(열) 목록
print(x.index) # 인덱스(행) 목록
print(x.values) # 값만 2차원으로 반환
print(x.head(2)) # 상위 n개만 반환
print(x.tail(2)) # 하위 n개만 반환
x.info() # 전처리(데이터 정리)하기 전에 결측치 확인

# [5] 인덱싱
print(x.iloc[1]) # iloc[인덱스번호]
print(x.iloc[1,2]) # iloc[행,열]
print(x.loc["a"]) # loc[라벨명]
print(x.loc["b","city"]) # loc[라벨명,컬럼명]

# [6] 슬라이싱, [시작인덱스, 끝인덱스]
print(x.iloc[0:2,0:1]) # [행슬라이싱, 열슬라이싱]
print(x.loc["a":"b","name":"city"]) # [행슬라이싱, 열슬라이싱]

# [7] 새로운 열 추가, ["새로운열"]=새로운값, .assign(새로운열=[새로운값])
x["score"]=[100,80,95] # 파괴적(원본 수정)
print(x)

x=x.assign(Score2=[87,65,78]) # 비파괴적(새롭게 재탄생)
print(x)

# [8] 특정한 값 수정, [기존열]=[수정할값]
x["age"]=[31,52,40]
print(x)

x.loc["b","age"]=70 # b행의 age열 값을70으로 변경
print(x)

x.iloc[0,0]="apple" # 0행의 0열 값을 apple 로 수정
print(x)

# 여러 개 한 번에 수정,
# loc[[시작라벨,끝라벨],수정컬럼라벨]=[새로운값]
# iloc[[시작인덱스, 끝인덱스], 컬럼인덱스]=[새로운값]
x.loc[["a","b"],"score"]=[10,20]
print(x)

# [9] 필터링, x[조건식], x[x[열이름]>논리]
cont1=x["Score2"]>70
print(cont1) # True, False, True
print(x[cont1]) # 데이터프레임[조건]

cont2=x["age"]>35 # 2번쨰 조건
print(x[cont1&cont2]) # 1번째 조건과 2번째 조건 논리 연산 가능
print(x[cont1|cont2])

# [10]
x.loc[x["Score2"]>70,"passed"]=True
x.loc[x["Score2"]<=70, "passed"]=False
print(x)

# [11] 열(컬럼) 이름 수정, .rename(index={}, columns={기존값:새로운값})
x=x.rename(columns={"city":"도시", "age":"나이"})
print(x)

# [12] 합계, .describe(): 수치자료들을 집계 요약
print(x.describe())

print(x["나이"].sum())
print(x["score"].mean())
print(x["passed"].value_counts()) # 특정 열의 빈도 확인
