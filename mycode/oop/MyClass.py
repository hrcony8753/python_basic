'''
클래스 선언
JAVA: class MyClass extends Object { }, class MyClass { }
PYTHON: class MyClass(object):, class MyClass:
'''
# class MyClass(object):
class MyClass:
    #constructor 선언
    def __init__(self):
        # attribute 초기화
        self.num = 100
        # private 속성 - 외부에서 접근 불가
        self.__name = 'dooly'

    # method (action) 선언
    def read_number(self):
        return self.num + 100

    # 부모 클래스(object)가 가진 __str__메서드를 재정의 하였음 (override)
    def __str__(self): # 유저가 이해할 수 있는 객체의 설명 / 유저에게 보여주기 위한 문자열
        return f'MyClass의 속성 Num:{str(self.num)}'

    # getter method
    @property
    def name(self):
        return self.__name
    
    # setter method
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    
# 객체 생성
myobj1 = MyClass()
print(myobj1)
print(myobj1.read_number())

# private 변수 사용
#print(myobj1.__name)  <error>
# getter 메서드 호출
print(myobj1.name) # method이나 변수처럼 사용가능

# setter 메서드 호출
myobj1.name = '길동'
print(myobj1.name)