# p251
# [1] min, max, sum
numbers=[103, 52, 273, 32, 77]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# p252
# [2] reversed(리스트), 이터레이터 변환
print(reversed(numbers)) # <list_reverseiterator object at 0x000001D0CB3E1390>
print(list(reversed(numbers))) # [77, 32, 273, 52, 103]

for i in reversed(numbers):
    print(i) # 역순 출력

# p254
# [3] enumerate(리스트), 인덱스 외 자료 순회 가능
print(enumerate(numbers)) # <enumerate object at 0x000001AE5510A480>
print(list(enumerate(numbers))) # [(0, 103), (1, 52), (2, 273), (3, 32), (4, 77)]

for index, value in enumerate(numbers):
    print(index, value)

# p256
# [4] items()
example_dict={"키A":"값A", "키B":"값B", "키C":"값C"}
print(example_dict.items()) # dict_items([('키A', '값A'), ('키B', '값B'), ('키C', '값C')])
for key, value in example_dict.items():
    print(key, value) # 키A 값A
                      # 키B 값B
                      # 키C 값C

# p257
# [5] 리스트 내 반복문 사용, 0부터 20 사이의 짝수 갖는 리스트
# (1)
array=[]
for i in range(0,20,2):
    array.append(i)
print(array) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# (2) [계산식 for 반복변수 in 반복할수있는것 if 조건식]
array=[i*i for i in range(0, 20, 2)]
print(array) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

array=[i for i in range(0, 20, 2) if i!=10]
print(array) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

array=[i for i in range(0, 20, 2) if i not in [10,12]]
print(array) # [0, 2, 4, 6, 8, 14, 16, 18] 여러 개 제외하고 싶을 때 not in

# p260
# [6] 문자열 여러 줄 입력하기
# (1) """ """
print("""안녕하세요1
      안녕하세요2""")

# (2) \n
print("안녕하세요1\n안녕하세요2")

# (3) () 소괄호 안에서 문자 여러 개 문자 연결 가능
print(("안녕하세요1\n""안녕하세요2"))

# (4) .join(문자열리스트), 리스트 내 요소 사이에 조합 문자열 연결
print("\n".join(["안녕하세요1", "안녕하세요2"]))

# p266
output =[i for i in range(1,101) if "{:b}".format(i).count("0")==1]
for i in output:
    print("{}:{}".format(i,"{:b}".format(i)))
print("합계",sum(output))