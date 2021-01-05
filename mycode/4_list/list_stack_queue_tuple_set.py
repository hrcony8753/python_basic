'''
Stack과 Queue를 list로 작성
Tuple과 Set을 list로 작성
'''
# stack
stack_list=[1,2,3,]
stack_list.append(5)
stack_list.extend([10,20])
print(stack_list)
stack_list.pop()
print(stack_list)
stack_list.pop()
print(stack_list)

#queue
queue_list = [10,20,30,]
queue_list.pop(0)
print(queue_list)

#tuple - read only list
my_tuple = tuple([10,30,40])
my_tuple2 = (20,30,40)
print(type(my_tuple),type(my_tuple2))
print(my_tuple2[2], my_tuple2[0:2], my_tuple*2)

# Error: tuple은 값 추가 안됨
# my_tuple2[0]=1

# comma의 차이
my_int=(10) # 정수형
my_tuple3=(10,)
print(type(my_int),type(my_tuple3))

#set - 중복 없는 리스트
my_set = set([1,2,3,1,2,3])
print(type(my_set),my_set)
my_set.add(4)
print(my_set)
my_set.add(1) # 중복된 값이므로 무시됨

my_set.remove(1)
print(my_set)

my_set.update([1,4,5,6,7])
print(my_set)

my_set.discard(3)
print(my_set)
my_set.clear()
print(my_set)

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])
print('합집합:', s1.union(s2), s1|s2)
print('교집합:', s1.intersection(s2), s1&s2)
print('차집합;', s1.difference(s2), s1-s2)
