# list, dictionary

# 1. 각 행을 딕셔너리로 표현
data1 = {'id':1, 'name':'hong kildong','email':'hong@mail.com','hp_num':'010-2343-9870'}
data2 = {'id':2, 'name':'lee soonsin','email':'lee@mail.com','hp_num':'010-3333-5555'}
data3 = {'id':3, 'name':'jang youngsil','email':'jang@mail.com','hp_num':'010-7777-1234'}
data4 = {'id':4, 'name':'king sejong','email':'king@mail.com','hp_num':'010-4567-0987'}

# 2. 4개의 딕셔너리를 포함한 리스트 만들기
data_list = [
    {'id':1, 'name':'hong kildong','email':'hong@mail.com','hp_num':'010-2343-9870'},
    {'id':2, 'name':'lee soonsin','email':'lee@mail.com','hp_num':'010-3333-5555'},
    {'id':3, 'name':'jang youngsil','email':'jang@mail.com','hp_num':'010-7777-1234'},
    {'id':4, 'name':'king sejong','email':'king@mail.com','hp_num':'010-4567-0987'}
]

# 3. 각 딕셔너리의 key, value 출력
for subject in data_list:
    print(subject)
    for k,v in subject.items():
        print(k, ":", v)
    print("")

