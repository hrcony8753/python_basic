''' lambda함수 (p.127),
    map 함수, reduce 함수

    <javascript코드 - map함수>
    //일반적인 function 선언
function add(x,y){
  return x+y;
}
console.log(add(10,20));

//람다식 function 선언 arrow(=>) function
let add2 = (x,y) => x+y; //param 1개라면 괄호 생략
console.log(add2(10,20));

//array 선언
let my_arr = [10,20,30,40]

let add_10 = x => x+10;
console.log(add_10(100));

//map() 함수
let result = my_arr.map(add_10);
console.log(result); //[20, 30, 40, 50]

//map()함수의 인자에 '사용자 정의 함수'를 전달할 수 있음
let result2 = my_arr.map(x => x + 10);
console.log(result2);
'''

# general
def add(x,y):
    return x+y
print(add(10,20))

# lambda 1 - 변수에 저장하고 출력
add2 = lambda x, y: x + y
print(add2(10,20))

# lambda 2 - 바로 출력
print((lambda x,y: x+y)(10,20))
print((lambda x:x**2)(10))


# map(function, list) 함수 - 각 element에 동일한 함수 적용
double_val = lambda x: x**2
print(double_val(2))
my_list = [1,2,3,4,5]
result = map(double_val,my_list)
print(result) # 객체 결과 반환
print(list(result)) # [1, 4, 9, 16, 25]


# map 함수를 사용하지 않는다면 (for loop)
result_list = []
for val in my_list:
    result_list.append(double_val(val))
print(result_list)


# my_list를 순회(iterate)하면서 값을 제곱값으로 반환하는 함수를 호출
result = list(map(lambda x: x ** 2, my_list))
print(result)


# [1,2,3,4,5], [10,20,30,40,50] 두 개의 리스트 더하기
# lambda 함수와 map 함수 사용
add = lambda x,y: x+y
print(add(1,10)) #1,10을 인수로 입력
my_list1 = [1,2,3,4,5]
my_list2 = [10,20,30,40,50]
result = list( map(add, my_list1, my_list2)) # 첫번째 방법
print(result)
result = list(map(add,[1,2,3,4,5],[10,20,30,40,50])) # 두번째 방법
print(result)
result = list( map(lambda x,y: x+y, my_list1, my_list2)) # 세번째 방법
print(result)


# map함수 if filter
double_even = lambda x: x **2 if x %2 ==0 else x
print(double_even(4), double_even(5))
print(list(map(double_even,my_list1)))


map_obj = map(double_even, my_list1)
print(next(map_obj), next(map_obj),next(map_obj))


# reduce() 함수 - 누적
from functools import reduce
add2 = lambda x,y : x+y
print(add2(10,20))
print(reduce(add2, my_list1))

result = reduce(lambda prev, curr: prev+curr, my_list1)
print(result)


# filter() 함수 - 원하는 조건 식에 해당하는 값만 반환
my_len = lambda my_str: len(my_str) > 6
print(my_len('hello'), my_len('mypthon'))

my_list_str = ['hello', 'mypython', 'Machine', 'Deep', 'DataScience']
# 6글자 이상인 문자열만 리스트에 저장하기
result = filter(my_len, my_list_str)
print(list(result))