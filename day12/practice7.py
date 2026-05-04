import pandas as pd
# 문제 1: 데이터프레임 생성과 정보 확인
# 리스트 x = [['iPhone', 120, 'Apple'], ['Galaxy', 110, 'Samsung'], ['Pixel', 90, 'Google']]를
# 활용하여 'Model', 'Price', 'Company' 컬럼명을 가진 DataFrame을 생성하고,
# 데이터의 전체적인 요약 정보(인덱스, 컬럼, 데이터 타입 등)를 한 번에 출력하는 메서드를 실행하시오.
x = [['iPhone', 120, 'Apple'], ['Galaxy', 110, 'Samsung'], ['Pixel', 90, 'Google']]
x=pd.DataFrame(x,columns=["Model","Price","Company"])
x.info()
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   Model    3 non-null      str  
#  1   Price    3 non-null      int64
#  2   Company  3 non-null      str 

# 문제 2: iloc와 loc를 이용한 데이터 추출
# 다음 DataFrame에서 'Bee'와 'Cat'의 'Name'과 'Age' 정보만 loc를 사용하여 추출하고,
# 동시에 전체 데이터의 2행 3열(City 정보)에 해당하는 값을 iloc으로 추출하여 출력하시오.
data = pd.DataFrame({
'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
'Age': [24, 27, 22, 32],
'City': ['Seoul', 'Busan', 'Incheon', 'Daejeon']
}, index=['A', 'B', 'C', 'D'])
print(data.loc["B":"C","Name":"Age"])
#   Name  Age
# B  Bee   27
# C  Cat   22
print(data.iloc[1,2]) # Busan

# 문제 3: 컬럼 추가와 조건부 값 수정
# 아래 데이터에서 'Score' 컬럼을 [85, 90, 95]로 추가한 뒤, 
# 'Score'가 90점 이상인 데이터의 'Name'을 'MVP'로 변경하시오.
data = pd.DataFrame({'Name': ['Ant', 'Bee', 'Cat'], 'Age': [24, 27, 22]})
data["Score"]=[85,90,95]
data.loc[data["Score"]>=90, "Name"]="MVP"
print(data)
#   Name  Age  Score
# 0  Ant   24     85
# 1  MVP   27     90
# 2  MVP   22     95

# 문제 4: 다중 조건을 활용한 행 필터링
# 아래 데이터에서 'Age'가 25세 이상이면서 동시에 'Score'가 80점 이상인 사람들의
# 데이터만 필터링하여 새로운 변수에 저장하고 출력하시오.
data = pd.DataFrame({
'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
'Age': [24, 27, 22, 32],
'Score': [85, 90, 88, 76]
})

print(data[(data["Age"]>=25)&(data["Score"]>=80)])
#   Name  Age  Score
# 1  Bee   27     90

# 문제 5: 데이터 병합 (Merge)
# 고객 정보가 담긴 df1과 구매 점수가 담긴 df2를 'ID' 컬럼을 기준으로 병합하되,
# 두 데이터에 모두 존재하는 ID만 남기는 방식(inner)과 df1의 모든 정보를 유지하는 방식(left)을
# 각각 수행하여 결과를 비교하시오.
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})
print(pd.merge(df1, df2, on="ID", how="inner"))
#    ID Name  Score
# 0   2  Bee     88
# 1   3  Cat     92
print(pd.merge(df1, df2, on="ID", how="left"))
#    ID Name  Score
# 0   1  Ant    NaN
# 1   2  Bee   88.0
# 2   3  Cat   92.0

# 문제 6: 데이터 연결 (Concat)
# 두 개의 성적표 df1, df2를 위아래(행 방향)로 합치고, 
# 기존 인덱스를 무시하고 새롭게 0부터 번호를 매기는 방식으로 연결하여 출력하시오.
df1 = pd.DataFrame({'Name': ['Ant', 'Bee'], 'Score': [90, 80]})
df2 = pd.DataFrame({'Name': ['Cat', 'Dog'], 'Score': [85, 75]})
print(pd.concat([df1,df2],axis=0,ignore_index=True))
#   Name  Score
# 0  Ant     90
# 1  Bee     80
# 2  Cat     85
# 3  Dog     75

# 문제 7: 다중 기준 정렬
# 아래 데이터에서 'Age'를 기준으로 오름차순 정렬하되, 
# 만약 'Age'가 같다면 'Score'를 기준으로 내림차순 정렬하여 출력하시오.
data = pd.DataFrame({
'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
'Age': [27, 27, 22, 32],
'Score': [88, 95, 85, 90]
})
result=data.sort_values(by=["Age","Score"],ascending=[True,False])
#   Name  Score
# 0  Ant     90
# 1  Bee     80
# 2  Cat     85
# 3  Dog     75

# 문제 8: 그룹화 및 집계 (Groupby)
# 'Category'별로 'Values'의 합계(sum), 평균(mean), 그리고 데이터 개수(count)를
# 한 번에 보여주는 요약 테이블을 생성하시오.
data = pd.DataFrame({
'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
'Values': [10, 20, 30, 40, 50, 60]
})
print(data.groupby("Category")["Values"].agg(["sum","mean","count"]))
#           sum  mean  count
# Category                  
# A          90  30.0      3
# B         120  40.0      3

# 문제 9: 다중 인덱스 그룹화
# 'Category'와 'Type' 두 가지 기준을 동시에 사용하여 그룹화한 뒤,
# 'Values'의 평균값을 구하여 출력하시오.
data = pd.DataFrame({
'Category': ['A', 'A', 'B', 'B'],
'Type': ['X', 'Y', 'X', 'Y'],
'Values': [10, 20, 30, 40]
})
print(data.groupby(["Category","Type"])["Values"].mean())
# Category  Type
# A         X       10.0
#           Y       20.0
# B         X       30.0
#           Y       40.0

# 문제 10: 빈도수 분석 및 컬럼명 변경
# 아래 데이터에서 'Fruit' 열의 고윳값별 빈도수를 구하여 확인하고,
# 최종적으로 모든 컬럼명을 ['Item', 'Style']로 변경하여 출력하시오.
data = pd.DataFrame({
'Fruit': ['apple', 'banana', 'apple', 'orange'],
'Color': ['red', 'yellow', 'red', 'orange']
})
print(data["Fruit"].value_counts())
data.columns=["Item","Style"] # data.columns 모든일, data. indexs 모든행
print(data)
#      Item   Style
# 0   apple     red
# 1  banana  yellow
# 2   apple     red
# 3  orange  orange

result=data.rename(columns={"Fruit":"Item", "Color":"Style"})
print(result)