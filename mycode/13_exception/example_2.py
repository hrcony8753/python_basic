'''
try~except문 없다면 바로 실행 오류
'''

for i in range(10):
    try:
        print(i, 10 // i)
    except ZeroDivisionError as err:
        print(err)
        print("Not divided by 0")
    finally:
        print("END~~")