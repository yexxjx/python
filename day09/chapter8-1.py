# p461
# 객체: 속성(상태)과 메소드(행동)로 이루어진 추상화
# 클래스: 객체를 프로그래밍에서 표현하기 위한 설계도
# 인스턴스: 클래스 기반으로 생성한 객체
# 생성자: 인스턴스가 생성될 때 실행되는 함수 = 초기화함수 역할

# [1] 클래스 만들기
class Student:
    # [2] 생성자 선언
    def __init__(self, name, korean, math, english, science): # 언더바(__) 앞 뒤로 2개씩
        # self: 자기 자신
        # self.변수명=매개변수명 , self.변수명(멤버변수 뜻)=매개변수명(인자값)
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
        # [4] 메소드 = 멤버함수 = 인스턴스 함수 = 함수
    def get_sum(self): # 해당 메소드를 호출한 인스턴스 가리킴, PYTHON: self vs JAVA: this
        return self.korean+self.math+self.english+self.science
    def get_average(self):
        return self.get_sum()/4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())
# [3] 인스턴스 생성하기
students=[
    Student("윤인성", 87, 98, 88, 95), # 인스턴스 생성, JAVA: new 클래스명(인자값) vs PYTHON: 클래스명(인자값)
    Student("연하진", 92, 98, 96, 98), # 관례적으로 클래스명은 첫글자 대문자
    Student("구지연", 76, 96, 94, 90)
]
# [5] 인스턴스 내 속성값 호출
print(students[0].name)
# [6] 인스턴스 내 메소드 호출
print(students[0].to_string())

# 클래스(인스턴스) vs 딕셔너리
# 클래스는 어떠한 구조를 미리 설계하여 통일되고 상태와 행동 오차를 줄일 수 있다
students=[
    {"name":"윤인성", "korean":87, "math":98,"english":88,"science":95},
    {"name":"연하진", "korean":92, "math":98,"english":96,"science":98},
    {"name":"구지연", "korean":76, "math":96,"english":94,"science":90}
    ]