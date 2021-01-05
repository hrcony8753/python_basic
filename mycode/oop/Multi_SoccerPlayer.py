'''
선수명, 선수 포지션, 선수 등번호 list로 선언
'''
names = ['홍길동','박지성','손흥민','둘리','파이썬']
positions = ['DF','MF','GK','DF','WF']
back_numbers = [5,10,20,30,15]

# class 없이 선수정보를 2차원 배열에 저장
for na, po, ba in zip(names, positions, back_numbers):
    print(na,po,ba)

players = [[name, position,back_number] for name, position, back_number in zip(names, positions, back_numbers)]
print(players)
player1 = players[0]
print(player1)
# 만일 홍길동의 back_number를 바꾸고 싶을 때
# player1[2] = 20 // 바람직하지 않음

# SoccerPlayer 클래스 import- python_class.py의 모든 코드가 출력되는 걸 방지하기 위해 def main(): 함수 정의
# from 패키지명.모듈명 import 클래스 or 함수
from mycode.oop.python_class import SoccerPlayer

player = SoccerPlayer('dooly','MF',10)
print(player)
# 객체를 여러 개 가지는 리스트 생성
players_obj = [SoccerPlayer(name,position,back_number) for name, position, back_number in zip(names, positions, back_numbers)]
print(players_obj)
player1 = players_obj[0]
# back_number 변경
player1.change_back_number(30)
print(player1)