'''List Comprehensions 연습문제
1. 250쪽 넘는 책 목록 만들기
2. 추천유무가 True인 책 목록 만들기
3. 출판사 목록 만들기 (중복되는 이름은 제거)
'''

books = list()
books.append({'제목':'개발자의 코드', '출판연도':'2013.02.28','출판사':'A 출판','쪽수':200, '추천유무':False})
books.append({'제목':'클린 코드', '출판연도':'2013.03.04','출판사':'B 출판','쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014.07.02','출판사':'A 출판','쪽수':296, '추천유무':True})
books.append({'제목':'구글드', '출판연도':'2010.02.10','출판사':'B 출판','쪽수':526, '추천유무':False})
books.append({'제목':'강의력', '출판연도':'2013.12.12','출판사':'C 출판','쪽수':248, '추천유무':True})

many_page_list = list()
recommend_list = list()
all_page_sum_value = int()
pub_name_set = set()

# general
for book in books:
    #print(book['쪽수'])
    if book['쪽수']>250:
        many_page_list.append(book['제목'])
    if book['추천유무']:
        recommend_list.append(book['제목'])
    all_page_sum_value += book['쪽수']
    pub_name_set.add(book['출판사'].strip()) #strip(): 공백제거(?)
 
print(f'250쪽 넘는 책 {many_page_list}')
print(f'추천하는 책 {recommend_list}')
print(f'전체 페이지 쪽수 {all_page_sum_value}')
print(f'출판사 목록(중복제거) {pub_name_set}')


# list comprehension
many_page_list = [book['제목'] for book in books if book['쪽수']>250]
print(f'250쪽 넘는 책 {many_page_list}')
recommend_list = [book['제목'] for book in books if book['추천유무']]
print(f'추천하는 책 {recommend_list}')
all_page_sum_value = sum(book['쪽수'] for book in books)
print(f'전체 페이지 쪽수 {all_page_sum_value}')
pub_name_set = set([book['출판사'] for book in books])
print(f'출판사 목록(중복제거) {pub_name_set}')

