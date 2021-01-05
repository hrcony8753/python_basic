# gugudan

while 1:
    num = int(input("구구단 몇 단을 계산할까요(1~9)?\n"))

    if 1 <= num <= 9:   # 1~9단 구구단
        print('구구단 {}단을 계산합니다.'.format(num))
        for j in range(1,10):
            print(num ,"X", j ,"=", num*j)
    elif num == 0 or num == 10: # 0,10단 구구단
        print("구구단 게임을 종료합니다.")
        break
