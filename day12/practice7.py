import pandas as pd
# 문제 1: 데이터프레임 생성과 정보 확인
# 리스트 x = [['iPhone', 120, 'Apple'], ['Galaxy', 110, 'Samsung'], ['Pixel', 90, 'Google']]를
# 활용하여 'Model', 'Price', 'Company' 컬럼명을 가진 DataFrame을 생성하고,
# 데이터의 전체적인 요약 정보(인덱스, 컬럼, 데이터 타입 등)를 한 번에 출력하는 메서드를 실행하시오.
x = [['iPhone', 120, 'Apple'], ['Galaxy', 110, 'Samsung'], ['Pixel', 90, 'Google']]
x=pd.DataFrame(x,columns=["Model","Price","Company"])
print(x)
#     Model  Price  Company
# 0  iPhone    120    Apple
# 1  Galaxy    110  Samsung
# 2   Pixel     90   Google

# 문제 2: iloc와 loc를 이용한 데이터 추출
# 다음 DataFrame에서 'Bee'와 'Cat'의 'Name'과 'Age' 정보만 loc를 사용하여 추출하고,
# 동시에 전체 데이터의 2행 3열(City 정보)에 해당하는 값을 iloc으로 추출하여 출력하시오.
data = pd.DataFrame({
'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
'Age': [24, 27, 22, 32],
'City': ['Seoul', 'Busan', 'Incheon', 'Daejeon']
}, index=['A', 'B', 'C', 'D'])
print(data.loc["Ant":"Cat","Name":"Age"])
#   Name  Age
# B  Bee   27
# C  Cat   22
print(data.iloc[1,2]) # Busan

# 문제 3: 컬럼 추가와 조건부 값 수정
# 아래 데이터에서 'Score' 컬럼을 [85, 90, 95]로 추가한 뒤, 
# 'Score'가 90점 이상인 데이터의 'Name'을 'MVP'로 변경하시오.
data = pd.DataFrame({'Name': ['Ant', 'Bee', 'Cat'], 'Age': [24, 27, 22]})
data["Score"]=[85,90,95]
print(data)
# data["Score"]>=90
# data.rename(columns={"Name":"MVP"})

# 문제 4: 다중 조건을 활용한 행 필터링
# 아래 데이터에서 'Age'가 25세 이상이면서 동시에 'Score'가 80점 이상인 사람들의
# 데이터만 필터링하여 새로운 변수에 저장하고 출력하시오.
data = pd.DataFrame({
'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
'Age': [24, 27, 22, 32],
'Score': [85, 90, 88, 76]
})

func1=data["Age"]>=25
func2=data["Score"]>=80
print(data[func1&func2])
#   Name  Age  Score
# 1  Bee   27     90