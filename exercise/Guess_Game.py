# Guess Game
import random

random_value = random.randint(1,100)    # 1~100 사이의 랜덤값 생성
#print(random_value)
cnt = 1
num = int(input("숫자를 맞혀보세요!:"))  # 사용자로부터 숫자 입력받기

while num != random_value:  # 오답인 경우
    if num > random_value:
        print("숫자가 너무 큽니다.")
        num = int(input("숫자를 맞혀보세요!:"))
    if num < random_value:
        print("숫자가 너무 작습니다.")
        num = int(input("숫자를 맞혀보세요!:"))
    cnt += 1
else:   # 정답인 경우
    print('정답입니다!', f'{cnt}번 만에 맞추셨습니다.')
