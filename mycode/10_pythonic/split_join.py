''' split과 join 함수
split함수: string-list
join함수: list-string
'''
# 기본적인 쓰임새 (SPLIT)
ex = 'hello i am HR'.split()    # 빈칸 기준으로 문자 나누기
print(ex)   # ['hello', 'i', 'am', 'HR']

ex2 = 'http://www.naver.com'.split('.')  # '.' 기준으로 문자 나누기
print(ex2)  #['http://www', 'naver', 'com']

# 기본적인 쓰임새 (JOIN)
ex_list = ['one', 'two', 'three', 'four', 'five']

result = ' '.join(ex_list)  # 빈칸으로 ex_list 연결
print(result)   # one two three four five

result = '**'.join(ex_list) # '**'으로 ex_list 연결
print(result)   # one**two**three**four**five

# 예제
my_str = 'java python kotlin'
my_list = my_str.split()
print(type(my_list), my_list)

my_str2= ''.join(my_list)
print(my_str2)
# javapythonkotlin

my_str='java, python, kotlin'
my_list = my_str.split(',')
print(type(my_list), my_list)

my_str2 = ','.join(my_list)
print(my_str2)
#java, python, kotlin


# replace () - 치환 함수
result = my_str.replace(',','?')
print(result)


