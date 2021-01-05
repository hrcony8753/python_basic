'''
range()함수: range(start, end, step)
'''
print(range(10))
for val in range(1,10,2):#한 칸씩 스킵하여 홀수 출력 (1~9까지)
    print(val)
else:
    print('for loop 종료')
    
# while~else 문
i = 1
while i<10:
    print(i)
    i += 2
else:
    print('while문 종료')

# dict 선언
wish_travel_cities = {
    #'키(k)':'값(v)'
    'Thai':'bangkok',
    'Korea':'seoul',
    'Japan':'tokyo'
}
print(wish_travel_cities.keys())
print(wish_travel_cities.values())
print(wish_travel_cities.items())

for key in wish_travel_cities.keys():
    print(f'{key}의 {wish_travel_cities[key]}(을)를 여행하고 싶어요.')

for k,v in wish_travel_cities.items():
    #print(k,v)
    print(f'{k}의 {v}(을)를 여행하고 싶어요.')

# guess game
import random
for val in range(10):
    random_value = random.randint(1,100) #1~100사이의 랜덤값 발생> 10번 반복
    print(random_value)

print(random.random()) #float형의 랜덤값
print(random.choice([1,2,3,4,5])) #choice 매개변수 중 랜덤값 선정
print(random.randint(1,10))

