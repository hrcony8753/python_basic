'''
list 타입을 선언하고 list에 엘리먼트 추가,삭제
'''
num_list = [60, 10, 30, 70, 80, ]
num_list2 = [1,2,3,4,5]
print(num_list==num_list2)
# 리스트 메모리 저장 방식 (p.46)
print(num_list, num_list2)
num_list2 = num_list #같은 주소를 가짐
print(num_list, num_list2)
num_list.sort() #정렬
print(num_list, num_list2) #num_list2도 정렬됨
num_list2 = [1,2,3,4,5]
num_list.sort()
print(num_list, num_list2) #num_list2에 다른 값 들어감 > 영향 없음

print(type(num_list), num_list)
print(num_list[0], num_list[0:3], num_list[3:])

for idx, num in enumerate(num_list):
    print(idx, num)

str_list = ['python', 'java', 'kotlin', 'C++', 'Scalar']
print(type(str_list), str_list)
# index로 list의 엘리먼트 값을 변경
str_list[1] = 'java script'
print(str_list[1], str_list[2:4])
# 엘리먼트 추가
str_list.append('Cobol')
str_list.insert(1, 'type script')
print(str_list)
# 엘리먼트 삭제
str_list.remove('Cobol')
print(str_list)
# 리스트 연산
print(str_list * 2)
print('Scholar' in str_list)




for idx, val in enumerate(str_list):
    print(idx, val)

mix_list = [100, 3.14, True, '파이썬']
for mix in mix_list:
    print(type(mix), mix)

# 리스트로 변환 (str->list)
my_list = list('Python')
print(type(my_list), my_list)
my_list2 = 'Hello, Python'.split(',')
print(my_list2)

# 패킹과 언패킹
# 패킹: 한 변수에 여러 개의 데이터를 넣는 것
my_list3 = ['aa','bb']
print(my_list3.index('bb')) #인덱스 찾기

#count
my_list4 = ['aa','bb','bb','ab']
print(my_list4.count('bb'))
my_list3.extend(my_list4) #리스트 자체 추가
print(my_list3)

#언패킹 - element 개수와 변수의 개수가 일치해야 함
#한 변수의 데이터가 각각의 변수로 반환
str1, str2 = ['cc','dd']
print(str1)
print(str2)
