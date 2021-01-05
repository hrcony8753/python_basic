'''
list_comprehensions : 리스트 안에 반복문이 포함됨
'''

# general (for+append)
result = []
for val in range(10):
    result.append(val)
print(result)   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# list comprehensions 1
result2 = [val for val in range(10)]
print(result2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result2 = [val for val in range(10) if val %2 is not 0]
print(result2)  # [1, 3, 5, 7, 9]


# list comprehensions 2
my_str1 = "Fine"
my_str2 = "Pine"
result = [i+j for i in my_str1 for j in my_str2]
print(result)   # ['FP', 'Fi', 'Fn', 'Fe', 'iP', 'ii', 'in', 'ie', 'nP', 'ni', 'nn', 'ne', 'eP', 'ei', 'en', 'ee']
result = [i+j for i in my_str1 for j in my_str2 if not(i==j)]   # 중복 제거
print(result)   # ['FP', 'Fi', 'Fn', 'Fe', 'iP', 'in', 'ie', 'nP', 'ni', 'ne', 'eP', 'ei', 'en']


# list comprehensions 3
words = 'Arguments can be passed to functions in four different ways'.split()
print(words)
my_list = [[w.upper(), w.lower(), w.title(),len(w)] for w in words]
print(my_list)
for word in my_list:
    print(word)

# list comprehensions 3 연습
words = 'Everything is possible, even the impossible.'.split()
print(words)    # ['Everything', 'is', 'possible,', 'even', 'the', 'impossible.']
ex_list = [[w.upper(), w.lower(), w.title(), len(w)] for w in words]
print(ex_list)
# [['EVERYTHING', 'everything', 'Everything', 10], ['IS', 'is', 'Is', 2],
# ['POSSIBLE,', 'possible,', 'Possible,', 9], ['EVEN', 'even', 'Even', 4],
# ['THE', 'the', 'The', 3], ['IMPOSSIBLE.', 'impossible.', 'Impossible.', 11]]


# enumerate 함수
words = 'Everything is possible, even the impossible.'.split()
for idx, w in enumerate(words,0):   # index 0부터 시작 (default)
    print(idx, w)
# 0 Everything
# 1 is
# 2 possible,
# 3 even
# 4 the
# 5 impossible.

print(list(enumerate(words,1))) # index 1부터 시작
# [(1, 'Everything'), (2, 'is'), (3, 'possible,'), (4, 'even'), (5, 'the'), (6, 'impossible.')]

word_dict = {idx: w for idx, w in enumerate(words,2)}   # 딕셔너리로 변환 & index 2부터 시작
print(word_dict)
# {2: 'Everything', 3: 'is', 4: 'possible,', 5: 'even', 6: 'the', 7: 'impossible.'}



# zip
my_list1 = [1,2,3]
my_list2 = [10,20,30]
my_list3 = [100,200,300]
print(zip(my_list1,my_list2,my_list3)) #zip결과를 바로 볼 수 없음

# zip 내용 확인 1
print(list(zip(my_list1,my_list2,my_list3)))    # [(1, 10, 100), (2, 20, 200), (3, 30, 300)]

# zip 내용 확인 2
for val in zip(my_list1,my_list2,my_list3):
    print(val, sum(val))
# (1, 10, 100) 111
# (2, 20, 200) 222
# (3, 30, 300) 333

# zip 내용 확인 2 - zip & list comprehension 이용
result = [[val,sum(val)] for val in zip(my_list1,my_list2,my_list3)]
print(result)   # [[(1, 10, 100), 111], [(2, 20, 200), 222], [(3, 30, 300), 333]]



# p.125
my_list1 = [1,2,3]
my_list2 = [10,20,30]
my_list3 = [100,200,300]

result_dict = {idx:sum(val) for idx,val in enumerate(zip(my_list1,my_list2,my_list3))}
print(result_dict)  # {0: 111, 1: 222, 2: 333}

a, b, c = zip(my_list1,my_list2,my_list3)
print(a)
print(b)
print(c)
# (1, 10, 100)
# (2, 20, 200)
# (3, 30, 300)
