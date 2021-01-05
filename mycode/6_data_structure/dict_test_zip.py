'''
dict타입: dict(), { }
'''
lang_dict = {}
lang_dict2 = dict()
print(type(lang_dict), type(lang_dict2))

# dict 값을 저장
lang_dict[100]='자바'
lang_dict[200]='파이썬'
lang_dict[200]='텐서플로우'
lang_dict[300]='PyTorch'
print(lang_dict)
#{100: '자바', 200: '텐서플로우', 300: 'PyTorch'} / lang_dict[200]값은 중복되어 먼저의 것은 무시됨

# dict에서 값을 읽기
print(lang_dict[300])
#print(lang_dict[400]) //key error
value = lang_dict.get(400)
print(value)
if value:
    print(value)
else:
    print('No Key')

for k,v in lang_dict.items():
    print(k,v)

print(200 in lang_dict)
print(400 in lang_dict)
print('자바'in lang_dict) #무조건 key값으로 찾기 때문에 false
print('자바'in lang_dict.values()) #value값으로 찾는 경우

# zip() 함수
days=['월요일','화요일','수요일']
fruits=['사과','바나나','딸기']
coffee=['아메리카노','라떼','모카','믹스']
print(zip(days, fruits, coffee), type(zip(days, fruits, coffee)))

for days, fruits, coffee in zip(days, fruits, coffee):
    print(days, fruits, coffee)

print(dict(zip(days,fruits))) #result 이상함! (위의 for문 주석처리)
print(list(zip(days,coffee))) #result 이상함!

days_tuple = '월요일','화요일','수요일'
coffees_tuple = '아메리카노','라떼','모카'
print(type(days_tuple)) #튜플형
print(list(zip(days_tuple, coffees_tuple)))
print(dict(zip(days_tuple, coffees_tuple)))

# zip()/range()함수는 iterable 객체를 반환하기 때문에 값을 확인하려면 for~in 구문 혹은 list()함수로 구현
print(range(10))
print(list(range(1,10,2)))


