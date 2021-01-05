'''List Comprehensions 연습문제
1. 50쪽 넘는 책 목록 만들기
2. 추천유무가 False인 책 목록 만들기
3. 출판사 목록 만들기 (중복되는 이름은 제거)
'''

books = list()  # 책 리스트 선언
# 책 목록 만들기
books.append({'제목':'Python', '출판사':'A 출판','쪽수':51, '추천유무':False})
books.append({'제목':'Java', '출판사':'B 출판','쪽수':15, '추천유무':True})
books.append({'제목':'C++', '출판사':'A 출판','쪽수':100, '추천유무':True})
books.append({'제목':'PHP', '출판사':'B 출판','쪽수':89, '추천유무':False})
books.append({'제목':'JSP','출판사':'C 출판','쪽수':30, '추천유무':True})

# 각 문제별 필요한 리스트 선언
page_list = list()
recommend_list = list()
pub_name_set = set()    # 중복 제거 목적

# general
for book in books:
    if book['쪽수']>50:
        page_list.append(book['제목'])
    if book['추천유무'] is False:
        recommend_list.append(book['제목'])
    pub_name_set.add(book['출판사'])

print(f'50쪽 넘는 책 {page_list}')
print(f'추천하지 않는 책 {recommend_list}')
print(f'출판사 목록(중복제거) {pub_name_set}')

# list comprehension
many_page_list = [book['제목'] for book in books if book['쪽수']>50]
print(f'250쪽 넘는 책 {page_list}')
recommend_list = [book['제목'] for book in books if book['추천유무'] is False]
print(f'추천하는 책 {recommend_list}')
pub_name_set = set([book['출판사'] for book in books])
print(f'출판사 목록(중복제거) {pub_name_set}')

'''
출력결과
250쪽 넘는 책 ['Python', 'C++', 'PHP']
추천하는 책 ['Python', 'PHP']
출판사 목록(중복제거) {'C 출판', 'B 출판', 'A 출판'}
'''
