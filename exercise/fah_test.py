# 1. import 모듈명
# import exercise.fahrenheit

# 2. import 모듈명 as 별칭
# import exercise.fahrenheit as fah

# 3. from 모듈명 import 함수명
# from fahrenheit import fah_convert

# 4. from 모듈명 import *
from fahrenheit import *

print('변환하고 싶은 섭씨 온도를 입력하세요!')
user_input = input()

# fah = ((9/5) * float(user_input)) + 32

# 3번 케이스
# result = fah_convert(user_input)

# 4번 케이스
result = fah_convert(user_input)
print(sayHello('파이썬'))

print('섭씨온도 ', user_input)
print('화씨온도 ', round(result, 2))
print('화씨온도 {:.2f} '.format(result))