'''
나이 계산: 현재년도 - 태어난년도 +1
태어난 년도를 입력 받음 input ()
from 모듈 import 클래스
'''
from datetime import datetime as dt
#현재년도: datetime 클래스에 선언된 today() 메서드 호출
current_year = dt.today().year
print(dt.today())
print(current_year)

year = int(input("태어난 년도를 입력하세요: "))
age = current_year - year + 1
if 17 <= age < 20:
    print("고등학생입니다.")
elif 20 <= age < 27:
    print("대학생입니다.")
else:
    print("학생이 아닙니다.")

