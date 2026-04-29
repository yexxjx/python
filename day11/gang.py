import numpy as np
data=np.genfromtxt(
    "./day11/person.csv",
    delimiter=",",
    skip_header=1,
    max_rows=19
)
print(data.shape)

# step1
person=(data[1:,1])
print("평균:", np.mean(person), "최대:",np.min(person))

# step2
# 전체 인구수의 5% 미만=((data[0][1])*0.05)
func1=((data[1:,1])<((data[0][1])*0.05))
# 20~39세 여성 인구 수/65세 이상 고령 인구 수
func2=(((data[1:,2])/(data[1:,4])*100)<50)
print("step2 결과:", func1&func2)

# step3
# '집중관리배열' - func1과 func2를 만족하는 값 중 최솟값의 0번째 행 반환
func3 = func1 & func2
selected = data[1:, 1][func3]
min_val = np.min(selected)
min_idx = np.argmin(selected)
original_idx = np.where(func3)[0][min_idx]
print("step3 결과:", min_val) # data 가 숫자로 되어있어서 문자인 지역 이름이 안나옵니다... 

# step4
func3=((data[1:,1])<((data[0][1])*0.05))
# 20~39세 여성 인구 수/65세 이상 고령 인구 수
func4=(((data[1:,2])/(data[1:,4])*100)<30)
print("step4 결과:", func3&func4)

# step5
data_min=np.min(data[1:20,1])
data_max=np.max(data[1:20,1])
print("min", data_max)
print("max", data_min)

norm_data=(person-data_max)/(data_min-data_max)
best_data=(norm_data>=0.9)
print("step5의 결과:", best_data)