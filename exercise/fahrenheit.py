'''
 섭씨를 입력 받아서 화씨로 변환하는 프로그램
 ctrl + shift + f10
'''

def fah_convert(value):
    # fah = ((9 / 5) * float(value)) + 32
    return ((9 / 5) * float(value)) + 32

def sayHello(msg):
    return f'Hello {msg}!'

'''
print('변환하고 싶은 섭씨 온도를 입력하세요!')
user_input = input()

# fah = ((9/5) * float(user_input)) + 32
result = fah_convert(user_input)

print('섭씨온도 ', user_input)
print('화씨온도 ', round(result, 2))
print('화씨온도 {:.2f} '.format(result))
'''
